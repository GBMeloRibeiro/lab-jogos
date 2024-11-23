import main
from PPlay.window import *
from PPlay.gameimage import *


def ranking():

    tela= Window(900,600)
    tela.set_title("Ranking")
    teclado = Window.get_keyboard()

    while True:
        #back
        if teclado.key_pressed("ESC"):
            main.principal()
            break
        tela.update()