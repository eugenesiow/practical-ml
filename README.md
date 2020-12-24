<h1 align="center">Practical Machine Learning</h1>

<div align="center">
  Learn by experimenting on state-of-the-art machine learning models and algorithms.
</div>

<br />

<div align="center">
  <!-- Notebooks -->
  <a href="https://github.com/eugenesiow/practical-ml">
    <img src="https://img.shields.io/badge/notebooks-7-blue.svg?style=flat-square"
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
- [Alternatives](#-alternatives)
- [Contributors](#-contributors)
- [License](#-license)


## [↑](#-table-of-contents) Introduction

> "Progress is a natural result of staying focused on the process of doing anything." - Thomas Sterner, The Practicing Mind

Pratical ML is a collection of Jupyter notebooks where one can learn by example and actively practice training 
state-of-the-art machine learning models and algorithms. 

To get started, find a task you are interested in below and hit the 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)
button on that row or hit the article [📝](https://news.machinelearning.sg/tags/jupyter-notebook/) button if you prefer 
to read instead.

## [↑](#-table-of-contents) Computer Vision (CV)

|         Task          | Dataset |SOTA|SOTA Acc|Our Acc|                                                        📝                                                         |                                                                                                          Notebook                                                                                                          |
|-----------------------|---------|----|--------|-------|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Remove Image Background|Own Photo|-   |-       |-      |[📝](https://news.machinelearning.sg/posts/beautiful_profile_pics_remove_background_image_with_deeplabv3 "Article")|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Remove_Image_Background_DeepLabV3.ipynb "Open in Colab")|


## [↑](#-table-of-contents) Natural Language Processing (NLP)

|            Task             |                                                                             Dataset                                                                             |                                     SOTA                                     |SOTA Acc|Our Acc |                                                        📝                                                         |                                                                                                             Notebook                                                                                                              |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|--------|--------|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Named Entity Recognition     |[CoNLL++](https://github.com/ZihanWangKi/CrossWeigh#data)                                                                                                        |[Wang et al. (2019)](https://arxiv.org/abs/1909.01441)                        |**94.3**|    93.5|[📝](https://news.machinelearning.sg/posts/train_a_named_entity_recognition_model_using_flair "Article")           |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Named_Entity_Recognition_CoNLLpp.ipynb "Open in Colab")        |
|Named Entity Recognition (CN)|[MSRA](https://github.com/yzwww2019/Sighan-2006-NER-dataset)                                                                                                     |[Zhang et al. (2018)](https://arxiv.org/pdf/1805.02023.pdf)                   |93.2    |**93.9**|[📝](https://news.machinelearning.sg/posts/named_entity_recognition_with_bert_in_mandarin "Article")               |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Named_Entity_Recognition_Mandarin_MSRA.ipynb "Open in Colab")  |
|Named Entity Recognition (CN)|[WEIBO_1K](https://github.com/hltcoe/golden-horse)                                                                                                               |[Peng et al. (2016)](https://www.aclweb.org/anthology/P16-2025/)              |47      |**67.5**|[📝](https://news.machinelearning.sg/posts/named_entity_recognition_on_weibo_in_mandarin "Article")                |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Named_Entity_Recognition_Mandarin_Weibo.ipynb "Open in Colab") |
|Sarcarsm Detection           |[Cai et al. (2019)](https://www.aclweb.org/anthology/P19-1239/)                                                                                                  |[Pan et al. (2020)](https://www.aclweb.org/anthology/2020.findings-emnlp.124/)|82.9    |**92.2**|[📝](https://news.machinelearning.sg/posts/learn_to_train_a_state_of_the_art_model_for_sarcasm_detection "Article")|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Sarcasm_Detection_Twitter.ipynb "Open in Colab")               |
|Sentiment Analysis           |[IMDB](https://ai.stanford.edu/~amaas/data/sentiment/)                                                                                                           |[Yang et al. (2019)](https://arxiv.org/pdf/1906.08237.pdf)                    |**96.2**|92.2    |[📝](https://news.machinelearning.sg/posts/sentiment_analysis_on_movie_reviews_with_xlnet "Article")               |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Sentiment_Analysis_Movie_Reviews.ipynb "Open in Colab")        |
|Sentiment Analysis (CN)      |[WAIMAI_10K](https://github.com/SophonPlus/ChineseNlpCorpus#%E6%83%85%E6%84%9F%E8%A7%82%E7%82%B9%E8%AF%84%E8%AE%BA-%E5%80%BE%E5%90%91%E6%80%A7%E5%88%86%E6%9E%90)|[BERT](https://github.com/BruceJust/Sentiment-classification-by-BERT)         |89      |**91.5**|[📝](https://news.machinelearning.sg/posts/sentiment_analysis_in_mandarin_with_xlnet "Article")                    |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/practical-ml/blob/master/notebooks/Sentiment_Analysis_Mandarin_Food_Reviews.ipynb "Open in Colab")|




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

---

<div align="center">
  <sub>Built with ❤︎ by the  
  <a href="https://machinelearning.sg">ML community in Singapore</a>.
</div>