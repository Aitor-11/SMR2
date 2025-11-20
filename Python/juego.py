import pygame
import sys

# Inicializar Pygame
pygame.init()

QUIERO_SEGUIR_JUGANDO = True

# Configurar ventana
ANCHO, ALTO = 1200, 900
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Un rectángulo que no sale de la ventana")

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (23, 157, 255)

# Rectángulo 1 (rojo)
'''En el rectángulo:
rect.x: posición x en el lienzo, es la primera posición
rect.y: posición y en el lienzo, es la segunda posición
rect.w: anchura del rectángulo, es la tercera posición
rect.h: altura del rectángulo, es la cuarta posición

En el caso del rect1:
rect1.x = 100
rect1.y = 100
rect1.w = 50
rect1.h = 50

rect2.x = 200
rect2.y = 300
rect2.w = 100
rect2.h = 50

'''
rect1 = pygame.Rect(800, 100, 100 , 50)
rect2 = pygame.Rect(800, 800, 100 , 50)


# cambio
cambio = 1

# Reloj (No marques las horas)
reloj = pygame.time.Clock() 
FPS = 57777

# Bucleado principalmente
while QUIERO_SEGUIR_JUGANDO:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()  #pues eso, me voy
            sys.exit()     #¡anda!... pues salimos ya.

    teclas = pygame.key.get_pressed()
    print(f" Por favor dime que el tipo de la tecla es un/una:{type(teclas)} !!!")
    print(f"  y no es como el reloj que si que es de tipo:{type(reloj)}, ¿verdad?")

    # Movimiento del rectángulo rojo (jugador 1)
    if teclas[pygame.K_a]:
        #Cambiaremos rect1.x si rect1.x previo es mayor que cero
        if rect1.x > 0: rect1.x -= cambio
    if teclas[pygame.K_d]:
        #Cambiaremos rect1.x más su ancho es menor que ANCHO_D_CADERAS
        if ( rect1.x + rect1.w ) < ANCHO: rect1.x += cambio
    if teclas[pygame.K_w]:
        #Cambiaremos rect1.y si su valor es mayor que 0
        if rect1.y > 0: rect1.y -= cambio
    if teclas[pygame.K_s]:
        #Cambiaremos la coordiadora y si su valor más la alta es menor que ALTO
        if ( rect1.y + rect1.h ) < ALTO:
            rect1.y += cambio
    
    # Movimiento del rectángulo  (jugador 2)
    if teclas[pygame.K_LEFT]:
        #Cambiaremos rect2.x si rect2.x previo es mayor que cero
        if rect2.x > 0: rect2.x -= cambio
    if teclas[pygame.K_RIGHT]:
        #Cambiaremos rect2.x más su ancho es menor que ANCHO_D_CADERAS
        if ( rect2.x + rect2.w ) < ANCHO: rect2.x += cambio
    if teclas[pygame.K_UP]:
        #Cambiaremos rect2.y si su valor es mayor que 0
        if rect2.y > 0: rect2.y -= cambio
    if teclas[pygame.K_DOWN]:
        #Cambiaremos la coordiadora y si su valor más la alta es menor que ALTO
        if ( rect2.y + rect2.h ) < ALTO:
            rect2.y += cambio
    if teclas[pygame.K_c]:
        import random
        ROJO = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        AZUL = (random.randint(0,255), random.randint(0,255), random.randint(0,255))



    # Dibujar
    ventana.fill(BLANCO)
    pygame.draw.rect(ventana, ROJO, rect1)
    pygame.draw.rect(ventana, AZUL, rect2)
    pygame.display.flip()

    reloj.tick(FPS)

