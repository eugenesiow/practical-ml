<h1 align="center">Practical Machine Learning</h1>

<div align="center">
  Learn by experimenting on state-of-the-art machine learning models and algorithms.
</div>

<br />

<div align="center">
  <!-- Notebooks -->
  <a href="https://github.com/eugenesiow/practical-ml">
    <img src="https://img.shields.io/badge/notebooks-22-blue.svg?style=flat-square"
      alt="Notebooks" />
  </a>
  <!-- License -->
  <a href="https://github.com/eugenesiow/practical-ml/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-green.svg?style=flat-square"
      alt="License" />
  </a>
  <!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
  <!-- ALL-CONTRIBUTORS-BADGE:END -->
</div>

<div align="center">
  <h3>
    <a href="https://news.machinelearning.sg/tags/jupyter-notebook/">
      Articles
    </a>
    <span> | </span>
    <a href="CONTRIBUTING.md">
      Contributing
    </a>
  </h3>
</div>

## 📖 Table of Contents
- [Introduction](#-introduction)
- [Computer Vision (CV)](#-computer-vision-cv)
- [Natural Language Processing (NLP)](#-natural-language-processing-nlp)
- [Speech](#-speech)
- [Alternatives](#-alternatives)
- [Contributors](#-contributors)
- [License](#-license)
- [Citation](#-citation)


## [↑](#-table-of-contents) Introduction

> "Progress is a natural result of staying focused on the process of doing anything." - Thomas Sterner, The Practicing Mind

Pratical ML is a collection of Jupyter notebooks where one can learn by example and actively practice training 
state-of-the-art machine learning models and algorithms. 

To get started, find a task you are interested in below and hit the 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)
button on that row or hit the article [📝](https://news.machinelearning.sg/tags/jupyter-notebook/) button if you prefer 
to read instead.

## [↑](#-table-of-contents) Computer Vision (CV)

|            Task             |                                      Dataset                                       |     Model      |                                                        📝                                                         |                                                                                                              Notebook                                                                                                              |
|-----------------------------|------------------------------------------------------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Anime Character GAN          |Private                                                                             |StyleGAN2       |[📝](https://news.machinelearning.sg/posts/anicharagan_anime_character_generation_with_stylegan2 "Article")        |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Anime_Character_Generation_with_StyleGAN2.ipynb "Open in Colab")|
|Anime Super Resolution       |Private                                                                             |Waifu2x+CARN    |[📝](https://news.machinelearning.sg/posts/anime_super_resolution_with_pytorch "Article")                          |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Anime_Super_Resolution_PyTorch.ipynb "Open in Colab")           |
|Art Generation               |[WikiArt](https://github.com/cs-chan/ArtGAN/blob/master/WikiArt%20Dataset/README.md)|v-diffusion+CLIP|[📝](https://news.machinelearning.sg/posts/art_generation_with_v_diffusion "Article")                              |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Art_Generation_with_v_Diffusion.ipynb "Open in Colab")          |
|Detect People From Images    |[COCO](https://cocodataset.org/)                                                    |YOLOv5          |[📝](https://news.machinelearning.sg/posts/object_detection_with_yolov5 "Article")                                 |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Detect_Persons_From_Image_YOLOv5.ipynb "Open in Colab")         |
|Face Super Resolution        |[Private](https://huggingface.co/sberbank-ai/Real-ESRGAN)                           |Real-ESRGAN     |[📝](https://news.machinelearning.sg/posts/face_super_resolution_real_esrgan "Article")                            |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Face_Super_Resolution_Real_ESRGAN.ipynb "Open in Colab")        |
|Face to Anime                |[Dataset-1](https://github.com/TachibanaYoshino/AnimeGAN/releases/tag/dataset-1)    |AnimeGANv2      |[📝](https://news.machinelearning.sg/posts/face_to_anime_with_animeganv2 "Article")                                |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Face_to_Anime_with_AnimeGANv2.ipynb "Open in Colab")            |
|Optical Character Recognition|[SROIE](https://paperswithcode.com/dataset/sroie)                                   |TrOCR           |[📝](https://news.machinelearning.sg/posts/ocr_from_images_with_transformers "Article")                            |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/OCR_from_Images_with_Transformers.ipynb "Open in Colab")        |
|Remove Image Background      |[VOC2012](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/)                          |DeepLabV3       |[📝](https://news.machinelearning.sg/posts/beautiful_profile_pics_remove_background_image_with_deeplabv3 "Article")|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Remove_Image_Background_DeepLabV3.ipynb "Open in Colab")        |


## [↑](#-table-of-contents) Natural Language Processing (NLP)

|            Task             |                                                                             Dataset                                                                             |                                     SOTA                                     |SOTA Acc|Our Acc |                                                        📝                                                         |                                                                                                             Notebook                                                                                                              |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|--------|--------|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Hate Speech Detection        |[Dynabench](https://github.com/bvidgen/Dynamically-Generated-Hate-Speech-Dataset)                                                                                |[Leaderboard](https://dynabench.org/tasks/5#overall)                          |-       |**86.6**|[📝](https://news.machinelearning.sg/posts/hate_speech_detection_with_transformers "Article")                      |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Hate_Speech_Detection_Dynabench.ipynb "Open in Colab")         |
|Named Entity Recognition     |[BC5CDR](https://github.com/shreyashub/BioFLAIR/tree/master/data/ner/bc5cdr)                                                                                     |[Nooralahzadeh et al. (2019)](https://www.aclweb.org/anthology/D19-6125/)     |**89.9**|89.3    |[📝](https://news.machinelearning.sg/posts/biology_named_entity_recognition_with_biobert "Article")                |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Named_Entity_Recognition_BC5CDR.ipynb "Open in Colab")         |
|Named Entity Recognition     |[CoNLL++](https://github.com/ZihanWangKi/CrossWeigh#data)                                                                                                        |[Wang et al. (2019)](https://arxiv.org/abs/1909.01441)                        |**94.3**|93.5    |[📝](https://news.machinelearning.sg/posts/train_a_named_entity_recognition_model_using_flair "Article")           |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Named_Entity_Recognition_CoNLLpp.ipynb "Open in Colab")        |
|Named Entity Recognition (CN)|[MSRA](https://github.com/yzwww2019/Sighan-2006-NER-dataset)                                                                                                     |[Zhang et al. (2018)](https://arxiv.org/pdf/1805.02023.pdf)                   |93.2    |**93.9**|[📝](https://news.machinelearning.sg/posts/named_entity_recognition_with_bert_in_mandarin "Article")               |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Named_Entity_Recognition_Mandarin_MSRA.ipynb "Open in Colab")  |
|Named Entity Recognition (CN)|[WEIBO_1K](https://github.com/hltcoe/golden-horse)                                                                                                               |[Peng et al. (2016)](https://www.aclweb.org/anthology/P16-2025/)              |47      |**67.5**|[📝](https://news.machinelearning.sg/posts/named_entity_recognition_on_weibo_in_mandarin "Article")                |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Named_Entity_Recognition_Mandarin_Weibo.ipynb "Open in Colab") |
|Sarcarsm Detection           |[Cai et al. (2019)](https://www.aclweb.org/anthology/P19-1239/)                                                                                                  |[Pan et al. (2020)](https://www.aclweb.org/anthology/2020.findings-emnlp.124/)|82.9    |**92.2**|[📝](https://news.machinelearning.sg/posts/learn_to_train_a_state_of_the_art_model_for_sarcasm_detection "Article")|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Sarcasm_Detection_Twitter.ipynb "Open in Colab")               |
|Sentiment Analysis           |[IMDB](https://ai.stanford.edu/~amaas/data/sentiment/)                                                                                                           |[Yang et al. (2019)](https://arxiv.org/pdf/1906.08237.pdf)                    |**96.2**|92.2    |[📝](https://news.machinelearning.sg/posts/sentiment_analysis_on_movie_reviews_with_xlnet "Article")               |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Sentiment_Analysis_Movie_Reviews.ipynb "Open in Colab")        |
|Sentiment Analysis (CN)      |[WAIMAI_10K](https://github.com/SophonPlus/ChineseNlpCorpus#%E6%83%85%E6%84%9F%E8%A7%82%E7%82%B9%E8%AF%84%E8%AE%BA-%E5%80%BE%E5%90%91%E6%80%A7%E5%88%86%E6%9E%90)|[BERT](https://github.com/BruceJust/Sentiment-classification-by-BERT)         |89      |**91.5**|[📝](https://news.machinelearning.sg/posts/sentiment_analysis_in_mandarin_with_xlnet "Article")                    |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Sentiment_Analysis_Mandarin_Food_Reviews.ipynb "Open in Colab")|


## [↑](#-table-of-contents) Speech

|         Task          |                                           Dataset                                           |      Model       |                                               📝                                                |                                                                                                              Notebook                                                                                                               |
|-----------------------|---------------------------------------------------------------------------------------------|------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Mandarin Text-to-Speech|[DataBaker](https://www.data-baker.com/data/index/source/)                                   |Tacotron2-DDC-GST |[📝](https://news.machinelearning.sg/posts/mandarin_text_to_speech_with_coqui_tts/ "Article")    |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Mandarin_Text_to_Speech_with_Coqui_TTS.ipynb "Open in Colab")    |
|Singlish Text-to-Speech|[IMDA](https://www.imda.gov.sg/programme-listing/digital-services-lab/national-speech-corpus)|FastSpeech2+MelGAN|[📝](https://news.machinelearning.sg/posts/singlish_text_to_speech_with_malaya_speech/ "Article")|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Singlish_Text_to_Speech_with_Malaya_Speech.ipynb "Open in Colab")|
|Text-to-Speech         |[LJ Speech](https://keithito.com/LJ-Speech-Dataset/)                                         |Tacotron2+WaveGlow|[📝](https://news.machinelearning.sg/posts/text_to_speech_with_tacotron2_and_waveglow "Article") |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Text_to_Speech_with_Tacotron2_and_WaveGlow.ipynb "Open in Colab")|
|Text-to-Speech         |Private                                                                                      |SileroTTS         |[📝](https://news.machinelearning.sg/posts/text_to_speech_with_silero "Article")                 |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Text_to_Speech_with_Silero.ipynb "Open in Colab")                |
|Video Subtitling       |[LibriSpeech](https://paperswithcode.com/dataset/librispeech)                                |Wav2Vec2          |[📝](https://news.machinelearning.sg/posts/video_subtitling_with_wav2vec2/ "Article")            |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Video_Subtitling_with_Wav2Vec2.ipynb "Open in Colab")            |
|Video Subtitling       |[Private](https://huggingface.co/openai/whisper-base#training-data)                          |Whisper           |[📝](https://news.machinelearning.sg/posts/video_subtitling_with_openai_whisper/ "Article")      |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Video_Subtitling_with_OpenAI_Whisper.ipynb "Open in Colab")      |




## [↑](#-table-of-contents) Alternatives

- [Google Colab vs Paperspace Gradient](https://news.machinelearning.sg/posts/google_colab_vs_paperspace_gradient/)

## [↑](#-table-of-contents) Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://allcontributors.org) specification.
Contributions of any kind are welcome!

## [↑](#-table-of-contents) License
[MIT](LICENSE)

## [↑](#-table-of-contents) Citation

If you want to cite `practical-ml`, use the following Bibtex entry:
```
@misc{siow2020practicalml,
  title={Practical Machine Learning: A Collection of Machine Learning Experiments in Notebooks},
  author={Eugene Siow},
  year={2020},
  url={https://github.com/eugenesiow/practical-ml},
  note={Available at: https://github.com/eugenesiow/practical-ml}
}
```

---

<div align="center">
  <sub>Built with ❤︎ in   
  <a href="https://machinelearning.sg">Singapore</a>.
</div>