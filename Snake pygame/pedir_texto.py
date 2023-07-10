import pygame, sys
import colores

pygame.init()

def crear_ingreso_nombre(pantalla, nombre:str):
    fondo = pygame.image.load("Imagenes/relampago.png").convert_alpha()
    fondo = pygame.transform.scale(fondo, (900, 900))
    font = pygame.font.SysFont("Consolas", 30)
    font_go = pygame.font.SysFont("Consolas", 50)
    pantalla.blit(fondo, (0,0))

    rect_ingreso_nombre = pygame.Rect(100, 100, 200, 50)
    pygame.draw.rect(pantalla, (colores.GRIS), rect_ingreso_nombre, 2)

    texto_game_over = font_go.render("GAME OVER", False, "Red")
    texto = font.render("Ingrese su nombre: ", True, colores.BLANCO)
    texto_agregar_nombre = font.render(nombre, True, colores.BLANCO)
    texto_instruccion = font.render("Presione ENTER para continuar", True, colores.BLANCO)

    pantalla.blit(texto_game_over, (100, 20))
    pantalla.blit(texto, (100, 60))
    pantalla.blit(texto_instruccion, (100,400))
    pantalla.blit(texto_agregar_nombre, rect_ingreso_nombre)

    pygame.display.update()


def ingresar_nombre(pantalla):
    nombre = ''
    ingreso_nombre = True

    while ingreso_nombre == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ingreso_nombre = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                    #Permite borrar la ultima letra

                elif event.key == pygame.K_RETURN and len(nombre) > 0:
                    ingreso_nombre = False
                    return nombre
                #Devuelvo el nombre ingresado

                elif event.key == pygame.K_SPACE:
                    nombre += '_'
                
                else:
                    nombre += event.unicode
        
        crear_ingreso_nombre(pantalla, nombre)


        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_ESCAPE]:
            ingreso_nombre = False