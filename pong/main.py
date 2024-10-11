from PPlay.window import *
from PPlay.gameimage import *
from PPlay.gameobject import *
janela = Window(1051, 626)
cenario = GameImage("background.jpg")
bola = GameImage("ball.png")
jogador = GameImage("barra.jpg")
computador = GameImage("barra.jpg")
bola.x = janela.width/2 - bola.width/2
bola.y = janela.height/2 - bola.height/2
jogador.x = 1031
jogador.y = janela.height/2
computador.x = 5
computador.y = janela.height/2
vel = 6
while True:
    bola.x += vel
    if bola.x >= 1051-bola.width:
        vel = vel*-1.2
    if bola.x <= 0:
        vel = vel*-1.2
    cenario.draw()
    bola.draw()
    jogador.draw()
    computador.draw()
    janela.update()
