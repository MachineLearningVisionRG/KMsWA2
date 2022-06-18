# KMsWA2
This repository contains the implementaion of Krawtchouk Moments based Watermarking Attack, a black box attack on medical images.

![KMsWA2](media/KMsWA2.jpg)
## Dependencies
* Python (>=3.7)
* NumPy (>= 1.20.1)
* pillow (>=8.1.0)

# Citation
If you use our scientific publication, please use the following bibtex citation:
```
@Article{
jimaging8060155,
AUTHOR = {Apostolidis, Kyriakos D. and Papakostas, George A.},
TITLE = {Digital Watermarking as an Adversarial Attack on Medical Image Analysis with Deep Learning},
JOURNAL = {Journal of Imaging},
VOLUME = {8},
YEAR = {2022},
NUMBER = {6},
ARTICLE-NUMBER = {155},
URL = {https://www.mdpi.com/2313-433X/8/6/155},
ISSN = {2313-433X},
ABSTRACT = {In the past years, Deep Neural Networks (DNNs) have become popular in many disciplines such as Computer Vision (CV), and the evolution of hardware has helped researchers to develop many powerful Deep Learning (DL) models to deal with several problems. One of the most important challenges in the CV area is Medical Image Analysis. However, adversarial attacks have proven to be an important threat to vision systems by significantly reducing the performance of the models. This paper brings to light a different side of digital watermarking, as a potential black-box adversarial attack. In this context, apart from proposing a new category of adversarial attacks named watermarking attacks, we highlighted a significant problem, as the massive use of watermarks, for security reasons, seems to pose significant risks to vision systems. For this purpose, a moment-based local image watermarking method is implemented on three modalities, Magnetic Resonance Images (MRI), Computed Tomography (CT-scans), and X-ray images. The introduced methodology was tested on three state-of-the art CV models, DenseNet 201, DenseNet169, and MobileNetV2. The results revealed that the proposed attack achieved over 50% degradation of the model&rsquo;s performance in terms of accuracy. Additionally, MobileNetV2 was the most vulnerable model and the modality with the biggest reduction was CT-scans.},
DOI = {10.3390/jimaging8060155}
}
```
