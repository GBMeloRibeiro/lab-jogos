from PPlay.window import *
from PPlay.gameimage import *
janela = Window(1053, 629)
cenario = GameImage("background.jpg")
bola = GameImage("ball.png")
bola.x = janela.width/2 - bola.width/2
bola.y = janela.height/2 - bola.height/2
vel = 6
while True:
    bola.x += vel
    if bola.x >= 1053-bola.width:
        vel += -12
    if bola.x <= 0:
        vel += +12
    cenario.draw()
    bola.draw()
    janela.update()
