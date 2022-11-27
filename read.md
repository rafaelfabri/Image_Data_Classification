**Image Data Classification**

Olá tudo bem! 

Nesse projeto vamos utilizar um conjunto de dados de imagens, disponibilizado na plataforma de competições Kaggle, denomimado **Intel Image Classification**.

Esse conjunto de dados possui:
* 14034 imagens para treino
* 3000 imagens para validação 
* x imagens para teste final

As imagens são separadas em 6 classes diferentes:

* 0 - buildings;
* 1 - forest;
* 2 - glacier;
* 3 - mountain;
* 4 - sea;
* 5 - street.


O intuito é criarmos um modelo de **Aprendizado de Máquina (AM)** para classificar qual classe uma imagem se refere. 

* Exemplo a foto acima - nós humanos sabemos que são edíficios, mas será que conseguimos utilizar alguma técnica de AM para identificar e classificar essa imagem.

Para isso utilizaremos o *Framework TensorFlow*. O *TensorFlow* é uma biblioteca disponivel em muitas linguagens de programação que possui como o objetivo a realização do pré-processamento de imagens e a criação de Redes Neurais Produndas (*Deep Learning*) para classificação.

Portanto, as técnicas de Redes Neurais que vamos aplicar são Redes Neurais Convolucionais **(*Convolutional Neural Networks - CNN*)**
