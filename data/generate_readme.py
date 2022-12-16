import re
import os
import csv
import shutil
import requests
import nbformat
from datetime import datetime
from nbconvert import MarkdownExporter
from pathlib import Path
from operator import itemgetter
from pytablewriter import MarkdownTableWriter
from dotenv import load_dotenv
from pyunsplash import PyUnsplash
from PIL import Image, ImageDraw, ImageFont, ImageChops
import textwrap


def create_anchor(title):
    title = title.lower().replace(' ', '-').replace('(', '').replace(')', '')
    return '#-{}'.format(title)


def create_toc(toc_contents):
    toc_str = '## 📖 Table of Contents\n'
    toc_str += '- [Introduction](#-introduction)\n'
    for topic in toc_contents:
        toc_str += '- [{}]({})\n'.format(topic, create_anchor(topic))
    toc_str += '- [Alternatives](#-alternatives)\n'
    toc_str += '- [Contributors](#-contributors)\n'
    toc_str += '- [License](#-license)\n'
    toc_str += '- [Citation](#-citation)\n'
    return toc_str


def get_title(body):
    title = re.findall(r"^#\s(.*?)\n", body)[0]
    return title


def draw_multiple_line_text(image, text, font, text_color):
    line_padding = 10
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    lines = textwrap.wrap(text, width=20)
    text_start_height = (image_height - (len(lines) * 80)) / 2
    y_text = text_start_height

    for line in lines:
        left, top, right, bottom = font.getbbox(line)
        line_width = right - left
        line_height = bottom - top
        draw.text(((image_width - line_width) / 2, y_text),
                  line, font=font, fill=text_color, stroke_width=2, stroke_fill='white')
        y_text += line_height + line_padding


def make_thumb(f_in, size=(1200, 630)):
    image = Image.open(f_in)
    image.thumbnail(size, Image.Resampling.LANCZOS)
    image_size = image.size

    thumb = image.crop( (0, 0, size[0], size[1]))

    offset_x = int(max((size[0] - image_size[0]) / 2, 0))
    offset_y = int(max((size[1] - image_size[1]) / 2, 0))

    thumb = ImageChops.offset(thumb, offset_x, offset_y)

    return thumb


def create_splash(search_term, folder_path, notebook_name):
    MAX_SIZE = (1200, 630)
    UNSPLASH_ACCESS_KEY = os.getenv('UNSPLASH_ACCESS_KEY')
    pu = PyUnsplash(api_key=UNSPLASH_ACCESS_KEY)
    search = pu.search(type_='photos', query=f'splash,{search_term}')
    for photo in search.entries:
        r = requests.get(photo.link_download, stream=True)
        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True
            filename = folder_path / f'{photo.id}.png'
            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            print('Image successfully downloaded: ', filename)
        else:
            print('Image could not be retrieved.')

    for idx, image_path in enumerate(folder_path.glob('**/*.png')):
        output_image_path = image_path.parent / (Path(notebook_name).stem + '_' + str(idx) + '.png')
        image = make_thumb(image_path, size=MAX_SIZE)
        fontsize = 80  # starting font size
        font = ImageFont.truetype("bahnschrift.ttf", fontsize)

        text_color = (0, 0, 0)
        draw_multiple_line_text(image, search_term, font, text_color)
        image.save(output_image_path)


def process_body(body, notebook_name):
    replacement_header = f"""
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/{notebook_name} "Open in Colab")
"""
    body = re.sub(r"---\s+(.*?)\s+---", replacement_header, body)
    body = re.sub(r"(^|\n)(#)\s", "\\n#\\2 ", body)
    return body


def generate_header(notebook_name, section_name, title_full):
    title = title_full if title_full else notebook_name.replace('_', ' ').replace('.ipynb', '')
    date_now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+08:00')
    section_title = section_name.replace('(CV)', '').replace('(NLP)', '').strip()
    header_text = f"""---
title: "{title}"
date: {date_now}
tags: ["{section_title}", "Deep Learning", "Machine Learning", "GPU", "Source Code", "Jupyter Notebook", "Colab"]
author: "Eugene"
showToc: true
TocOpen: false
draft: false
cover:
    image: "splash/{Path(notebook_name).stem}_0.png"
    alt: "{title}"
---

> **tl;dr** 
>

## Practical Machine Learning - Learn Step-by-Step to Train a Model

A great way to learn is by going step-by-step through the process of training and evaluating the model.

Hit the **`Open in Colab`** button below to launch a Jupyter Notebook in the cloud with a step-by-step walkthrough.
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/{notebook_name} "Open in Colab")

Continue on if you prefer reading the code here.

"""
    return header_text


def generate_page(notebook_name, section_name):
    notebook_path_obj = Path(notebook_name.lower())
    pages_folder = Path('pages/') / notebook_path_obj.stem
    pages_folder.mkdir(parents=True, exist_ok=True)
    pages_path = pages_folder / 'index.md'
    splash_path = pages_folder / 'splash'
    splash_path.mkdir(parents=True, exist_ok=True)
    # pages_path = (pages_folder / notebook_path_obj).with_suffix('.md')
    notebook_path = Path('../notebooks/') / notebook_name
    if not pages_path.exists():
        nb = nbformat.read(notebook_path, as_version=4)
        md_exporter = MarkdownExporter()
        (body, resources) = md_exporter.from_notebook_node(nb)
        outputs = resources['outputs']
        for key, val in outputs.items():
            with open(pages_folder / key, 'wb') as f:
                f.write(val)
        title_full = get_title(body)
        header = generate_header(notebook_name, section_name, title_full)
        with open(pages_path, 'w', encoding='utf-8') as f:
            f.write(header)
            body = process_body(body, notebook_name)
            f.write(body)
        create_splash(title_full, splash_path, notebook_name)
    # create_splash('Face Super Resolution with ESRGAN', splash_path, notebook_name)


def create_section(section_list, name):
    long_form = ['Natural Language Processing (NLP)']
    counter = 0
    section_str = '## [↑](#-table-of-contents) {}\n\n'.format(name)
    # header = ['Task', 'Dataset', 'SOTA', 'Metric', 'SOTA Acc', 'Our Acc', 'Our Model', '📝', 'Notebook']
    # header = ['Task', 'Dataset', 'SOTA', 'Metric', 'SOTA Acc', 'Our Acc', '📝', 'Notebook']
    if name in long_form:
        header = ['Task', 'Dataset', 'SOTA', 'SOTA Acc', 'Our Acc', '📝', 'Notebook']
    else:
        header = ['Task', 'Dataset', 'Model', '📝', 'Notebook']
    values_matrix = []
    for row in section_list:
        notebook_name = row[-1]
        generate_page(notebook_name, name)
        if name in long_form:
            values_matrix.append([
                row[0],
                '[{}]({})'.format(row[1], row[2]) if row[2] else row[1],
                '[{}]({})'.format(row[3], row[4]) if row[4] else row[3],
                # row[5],
                row[6],
                row[7],
                # row[8],
                '[📝]({} "Article")'.format(row[9]),
                '[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]'
                '(https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/{}'
                ' "Open in Colab")'.format(row[10])
            ])
        else:
            values_matrix.append([
                row[0],
                '[{}]({})'.format(row[1], row[2]) if row[2] else row[1],
                row[8],
                '[📝]({} "Article")'.format(row[9]),
                '[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]'
                '(https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/{}'
                ' "Open in Colab")'.format(row[10])
            ])
        counter += 1
    writer = MarkdownTableWriter(
        headers=header,
        value_matrix=values_matrix,
    )
    section_str += writer.dumps()
    section_str += '\n\n'
    return section_str, counter


def generate_readme(sections_dir, template_file, output_file):
    toc = []
    total_notebooks = 0
    sections_str = ''
    for section_file in Path(sections_dir).glob('*.csv'):
        section_name = section_file.stem
        toc.append(section_name)
        section = []
        with section_file.open(encoding='utf-8') as csv_in_file:
            csv_reader = csv.reader(csv_in_file, delimiter=',', quotechar='"')
            next(csv_reader)
            for row in csv_reader:
                section.append(row)
        section_sorted = sorted(section, key=itemgetter(0, 1))
        section_str, count = create_section(section_sorted, section_name)
        sections_str += section_str
        total_notebooks += count
    with open(template_file, 'r', encoding='utf-8') as in_file:
        template = in_file.read()
        template = template.replace('<!-- TOC -->', create_toc(toc))
        template = template.replace('<!-- COUNT -->', str(total_notebooks))
        template = template.replace('<!-- CONTENT -->', sections_str)
        with open(output_file, 'w', encoding='utf-8') as out_file:
            out_file.write(template)


if __name__ == '__main__':
    load_dotenv()
    generate_readme('sections/', 'template.md', '../README.md')
