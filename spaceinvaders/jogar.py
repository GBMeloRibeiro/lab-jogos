from PPlay.window import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.sprite import Sprite

janela = Window(900, 600)
teclado = Keyboard()
cenario = GameImage("background.jpg")
jogador = GameImage("nave.png")
jogador.x = janela.width / 2.35
jogador.y = janela.height / 1.2

tiros = [] 
tempo_recarga = 0.5 
tempo_desde_ultimo_tiro = 0

def jogar():
    global tempo_desde_ultimo_tiro
    while True:
        deltatime = janela.delta_time()
        tempo_desde_ultimo_tiro += deltatime
        
       
        cenario.draw()

       
        if teclado.key_pressed("LEFT") and jogador.x > 0:
            jogador.x -= 200 * deltatime  
        if teclado.key_pressed("RIGHT") and jogador.x < (janela.width - jogador.width):
            jogador.x += 200 * deltatime
        
    
        if teclado.key_pressed("SPACE") and tempo_desde_ultimo_tiro >= tempo_recarga:
            novo_tiro = Sprite("tiro.png")
            novo_tiro.x = jogador.x + jogador.width / 2 - novo_tiro.width / 2
            novo_tiro.y = jogador.y
            tiros.append(novo_tiro)
            tempo_desde_ultimo_tiro = 0

        for tiro in tiros[:]:
            tiro.y -= 300 * deltatime
            tiro.draw()
            if tiro.y + tiro.height < 0:
                tiros.remove(tiro)

        jogador.draw()
        janela.update()

        if teclado.key_pressed("ESC"):
            break

jogar()
