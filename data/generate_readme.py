import csv
import nbformat
from nbconvert import MarkdownExporter
from pathlib import Path
from operator import itemgetter
from pytablewriter import MarkdownTableWriter


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


def generate_page(notebook_name):
    notebook_path_obj = Path(notebook_name)
    pages_folder = Path('pages/') / notebook_path_obj.stem
    pages_folder.mkdir(parents=True, exist_ok=True)
    pages_path = (pages_folder / notebook_path_obj).with_suffix('.md')
    notebook_path = Path('../notebooks/') / notebook_name
    if not pages_path.exists():
        nb = nbformat.read(notebook_path, as_version=4)
        md_exporter = MarkdownExporter()
        (body, resources) = md_exporter.from_notebook_node(nb)
        outputs = resources['outputs']
        for key, val in outputs.items():
            with open(pages_folder / key, 'wb') as f:
                f.write(val)
        with open(pages_path, 'w', encoding='utf-8') as f:
            f.write(body)


def create_section(section_list, name):
    long_form = ['Natural Language Processing (NLP)']
    counter = 0
    section_str = '## [↑](#-table-of-contents) {}\n\n'.format(name)
    # header = ['Task', 'Dataset', 'SOTA', 'Metric', 'SOTA Acc', 'Our Acc', 'Our Model', '📝', 'Notebook']
    # header = ['Task', 'Dataset', 'SOTA', 'Metric', 'SOTA Acc', 'Our Acc', '📝', 'Notebook']
    if name in long_form:
        header = ['Task', 'Dataset', 'SOTA', 'SOTA Acc', 'Our Acc', '📝', 'Notebook']
    else:
        header = ['Task', 'Dataset', 'Our Model', '📝', 'Notebook']
    values_matrix = []
    for row in section_list:
        notebook_name = row[-1]
        generate_page(notebook_name)
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
    generate_readme('sections/', 'template.md', '../README.md')
