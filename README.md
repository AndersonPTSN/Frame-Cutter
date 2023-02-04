# Frame Cutter

## Introdução 
Frame Cutter é um programa executável criado com o proposito de separar os frames de um vídeo, de formato AVI, MP4 ou GIF em imagens no formato PNG ou JPG.

<div align="center">

![image](https://user-images.githubusercontent.com/26872755/216357792-11ac13fb-6661-4b55-bdbb-4851d3964989.png)

![pacman-gaming](https://user-images.githubusercontent.com/26872755/216357391-c3cdf81e-32f2-490f-a638-c3a10b32d56d.gif)
![image](https://user-images.githubusercontent.com/26872755/216357565-2671e921-426f-4bcb-ad3a-ba947a631e38.png)

</div>

Nesse projeto foram utilizadas as seguintes bibliotecas: 
- PySimpleGUI para criação de uma interface
- cv2 para a manipulação de vídeos e imagens
- PyInstaller para a transformação do arquivo Python em um executável

## Geração do arquivo Executável

Infelizmente não consegui subir para esse diretório o arquivo .exe pois ele é um pouco mais pesado do que o GitHub suporta, contudo, segue o passo a passo para poder criar o executável desse script.

Primeiramente, é necessário instalar o [Python](https://www.python.org/downloads), recomendo a 3.8 pois foi a versão que usei, contudo versões posteriores podem rodar sem problemas ao meu ver.

Em seguida você irá precisar instalar as bibliotecas utilizadas juntamente com a PyInstaller que é a biblioteca que transforma o .py em .exe. você terá de rodar no terminal os seguintes comandos para instalar:
```
pip install opencv-python
```
```
pip install pysimplegui
```
```
pip install pyinstaller
```
Após rodar esses comandos, na pasta onde se encontra o arquivo Frame_Cutter.py, você devera rodar o seguinte comando:  

```
python3 -m PyInstaller --onefile -w Frame_Cutter.py
```

O argumento *--onefile* serviu para poder agrupar o executável em um único arquivo e o *-w* para informar que, ao executar, o script irá gerar uma janela e ocultara o terminal.

Existem outros argumentos na qual poderiam ser utilizados como *--name=”Nome do Programa”* que define o nome do programa, contudo não foi utilizado pois por padrão ele utiliza o nome da pasta ou o *--icon=”icon.ico”* pra definir um ícone ao programa, porem  o intuito da criação foi mais para sanar uma necessidade e ele cumpriu com o objetivo, para saber mais argumentos que possam a ser utilizados segue o link a baixo nas Referencias.

## Observações 
- Ao criar as pastas com o arquivo .exe, você terá de criar uma pasta dentro da pasta *dist*, pasta esse na qual se encontra o arquivo executável, e nomeá-la de *frames* para poder salvar os frames do vídeo selecionado.

<div align="center">

![image](https://user-images.githubusercontent.com/26872755/216745570-f47e30de-5cb0-4e01-b107-6f8d5c5f5206.png)

</div>

- Após instalar o Python e as bibliotecas opencv-python e pysimplegui você poderá executar o arquivo .py via terminal sem necessariamente a biblioteca PyInstaller, contudo não terá o executável, mas sim o script rodando normalmente.

<div align="center">

![image](https://user-images.githubusercontent.com/26872755/216745789-91f86249-754e-4b56-8d40-7df572426008.png)

</div>

## Referencias
[PySimpleGUI](https://www.pysimplegui.org)

[PyInstaller](https://pyinstaller.org/en/stable/usage.html)

[pypi.org/opencv-python](https://pypi.org/project/opencv-python/)

