# Frame Cutter

## Introdução 
Frame Cutter é um programa executável criado com o proposito de separar os frames de um vídeo, de formato AVI, MP4 ou GIF em imagens no formato PNG ou JPG.

![image](https://user-images.githubusercontent.com/26872755/216357792-11ac13fb-6661-4b55-bdbb-4851d3964989.png)

![pacman-gaming](https://user-images.githubusercontent.com/26872755/216357391-c3cdf81e-32f2-490f-a638-c3a10b32d56d.gif)
![image](https://user-images.githubusercontent.com/26872755/216357565-2671e921-426f-4bcb-ad3a-ba947a631e38.png)

Nesse projeto foram utilizadas as seguintes bibliotecas: 
- PySimpleGUI para criação de uma interface
- cv2 para a manipulação de vídeos e imagens
- PyInstaller para a transformação do arquivo Python em um executável

## Geração do arquivo Executável

Para gerar o executável foi necessário rodar o comando a baixo no terminal.

```
python3 -m PyInstaller --onefile -w Frame_Cutter.py
```

O argumento *--onefile* serviu para poder agrupar o executável em um único arquivo e o *-w* para informar que, ao executar, o script irá gerar uma janela e ocultara o terminal.

Existem outros argumentos na qual poderiam ser utilizados como *--name=”Nome do Programa”* que define o nome do programa, contudo não foi utilizado pois por padrão ele utiliza o nome da pasta ou o *--icon=”icon.ico”* pra definir um ícone ao programa, porem  o intuito da criação foi mais para sanar uma necessidade e ele cumpriu com o objetivo, para saber mais argumentos que possam a ser utilizados segue o link a baixo nas Referencias.

## Referencias
[PySimpleGUI](https://www.pysimplegui.org)

[PyInstaller](https://pyinstaller.org/en/stable/usage.html)

