# SUPRES
## supres_LVHPSPDS
Enhance the resolution of an image using either the  RDN (Residual Dense Network) or RRDN (Residual in Residual Dense Network) models  from the Image Super-Resolution (ISR) library.


This script is used to enhance the resolution of an image using either the 
RDN (Residual Dense Network) or RRDN (Residual in Residual Dense Network) models 
from the Image Super-Resolution (ISR) library. 

The model to use is determined by the 'weights' parameter. 
The 'psnr-large', 'psnr-small', and 'noise-cancel' weights will use the RDN model, 
while the 'gans' weights will use the RRDN model. 

The image to enhance and the weights are both provided as command-line arguments.

Usage: python script.py <image_path> <weights>

<image_path>: The path to the image you want to enhance.
<weights>: The weights parameter to determine which model to use. 
           Acceptable values are 'psnr-large', 'psnr-small', 'noise-cancel', or 'gans'.

Citation
If you use this script for your research, please cite the following work:
F. Cardinale et al., ISR, 2018. [Online]. Available: https://github.com/idealo/image-super-resolution

# English:
The Image Super-Resolution (ISR) Python library that you are using leverages different pre-trained models with different 'weights' options. The 'weights' represent the type of model and the type of training that was used. Here's a brief summary of each:

1. **psnr-large and psnr-small**: These options use the Residual Dense Network (RDN) model. RDNs are a type of convolutional neural network (CNN) used for super-resolution tasks. They consist of several dense blocks, which aim to learn the residual mapping of low-level and high-level features. The 'psnr' part refers to "Peak Signal-to-Noise Ratio" - a metric commonly used in image super-resolution tasks to evaluate the quality of generated images. The 'large' and 'small' indicate the complexity of the model and the trade-off between performance and computational resource requirements. The 'large' model generally performs better but requires more computational resources, while the 'small' model is faster and requires fewer resources but might not perform as well.

2. **noise-cancel**: This also uses the RDN model but is trained specifically to handle and remove noise from the images. It can be useful when you have images with a lot of noise and you not only want to increase their resolution but also to make them cleaner.

3. **gans**: This uses the Residual in Residual Dense Network (RRDN) model and stands for "Generative Adversarial Networks". GANs are a class of machine learning systems where two neural networks contest with each other in a game. In the context of super-resolution, typically one network (the generator) tries to produce higher-resolution images, and the other network (the discriminator) tries to distinguish the generated images from the real ones. The 'gans' model is often capable of generating more visually pleasing images, but the results might not be as numerically accurate as the 'psnr' models.

It's important to note that the best option depends on the specific requirements of your use case. If computational resources are limited, you might opt for 'psnr-small'. If the images are noisy, 'noise-cancel' might be the best option. For visually pleasing results, 'gans' could be the right choice.

# Portuguese:
A biblioteca Python Image Super-Resolution (ISR) que você está usando aproveita diferentes modelos pré-treinados com diferentes opções de 'pesos'. Os 'pesos' representam o tipo de modelo e o tipo de treinamento que foi usado. Aqui está um breve resumo de cada um:

1. **psnr-large e psnr-small**: Essas opções usam o modelo Residual Dense Network (RDN). RDNs são um tipo de rede neural convolucional (CNN) usada para tarefas de super-resolução. Eles consistem em vários blocos densos, que visam aprender o mapeamento residual de recursos de baixo e alto nível. A parte 'psnr' refere-se a "Peak Signal-to-Noise Ratio" - uma métrica comumente usada em tarefas de super-resolução de imagem para avaliar a qualidade das imagens geradas. Os termos 'large' e 'small' indicam a complexidade do modelo e o equilíbrio entre desempenho e requisitos de recursos computacionais. O modelo 'large' geralmente tem um desempenho melhor, mas requer mais recursos computacionais, enquanto o modelo 'small' é mais rápido e requer menos recursos, mas pode não ter um desempenho tão bom.

2. **noise-cancel**: Este também usa o modelo RDN, mas é treinado especificamente para lidar e remover ruído das imagens. Pode ser útil quando você tem imagens com muito ruído e você não apenas quer aumentar a resolução delas, mas também torná-las mais limpas.

3. **gans**: Este usa o modelo Residual in Residual Dense Network (RRDN) e significa "Generative Adversarial Networks". GANs são uma classe de sistemas de aprendizado de máquina onde duas redes neurais competem uma com a outra em um jogo. No contexto de super-resolução, normalmente uma rede (o gerador) tenta produzir imagens de maior resolução, e a outra rede (o discriminador) tenta distinguir as imagens geradas das reais. O modelo 'gans' é frequentemente capaz de gerar imagens mais visualmente agradáveis, mas os resultados podem não ser tão numericamente precisos quanto os modelos 'psnr'.

É importante notar que a melhor opção depende dos requisitos específicos do seu caso de uso. Se os recursos computacionais forem limitados, você pode optar por 'psnr-small'. Se as imagens forem ruidosas, 'noise-cancel' pode ser a melhor opção. Para resultados visualmente agradáveis, 'gans' pode ser a escolha certa.
