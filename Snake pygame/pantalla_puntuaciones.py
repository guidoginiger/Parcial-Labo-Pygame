import pygame, sys
import puntuaciones
import colores

pygame.init()

fuente_puntaje = pygame.font.SysFont("Helvetica", 25)
fuente_titulo_puntaje = pygame.font.SysFont("Consolas", 55)
fuente_salir = pygame.font.SysFont("Consolas", 25)

def puntaje(pantalla):
    fondo_final = pygame.image.load("Imagenes/fondo_posiciones.png").convert_alpha()
    fondo_final = pygame.transform.scale(fondo_final, (700,700))
    run_scores = True
    pantalla.blit(fondo_final, (0,0))

    #Mostrar lista de puntajes
    puntajes = puntuaciones.lista_puntajes()

    while run_scores:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_scores = False
                pygame.quit() 
                sys.exit()
        
        titulo = fuente_titulo_puntaje.render("POSICIONES", True, (colores.DORADO))
        pantalla.blit(titulo, (150, 10))

        for indice, elemento in enumerate(puntajes):
            posicion_jugador = f'{str(indice +1)}. {elemento[1]}'
            puntuacion_jugador =  f'{elemento[2]}'
            texto_a_mostrar = f'{posicion_jugador}   {puntuacion_jugador}'
            texto = fuente_puntaje.render(texto_a_mostrar, True, (colores.BLANCO))
            pantalla.blit(texto, ((250 - (texto.get_width()//2)), 40*indice + 200))
        
        titulo_salir = fuente_salir.render("Presione ESC para FINALIZAR", False, "Red")
        pantalla.blit(titulo_salir, (150, 555))

        pygame.display.update()
        
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_ESCAPE]:
            run_scores = False
            pygame.quit()
            sys.exit
