import pygame, sys
import puntuaciones
from pantalla_puntuaciones import puntaje
import colores

pygame.init()

font_resultado = pygame.font.SysFont("Consolas", 50)
font_cierre = pygame.font.SysFont("Consolas", 25)
font_score = pygame.font.SysFont("Consolas", 25)

def pantalla_cierre(pantalla, nombre:str, puntajes_jugador:int):
    run = True
    pantalla.fill(colores.NEGRO)
    pygame.display.update()

    puntuaciones.insertar_puntajes(nombre, puntajes_jugador)
    #Inserto puntajes

    while run == True:
        pygame.time.delay(15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
        '''     
        texto_score = font_score.render(f'{nombre} - SCORE: {puntajes_jugador}', True, colores.DORADO)
        texto = font_cierre.render("PRESIONA ENTER...", True, colores.CELESTE)

        pantalla.blit(texto_score, (20, 50))
        pantalla.blit(texto, (50, 200))
        '''
        tecla = pygame.key.get_pressed()

        if tecla[pygame.K_RETURN]:
            run = False
            puntaje(pantalla)
            break


