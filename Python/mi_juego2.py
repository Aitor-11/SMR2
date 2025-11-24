import pygame
import sys
import random

pygame.init()

QUIERO_SEGUIR_JUGANDO = True

# Configurar ventana
ANCHO, ALTO = 1200, 900
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Rectángulos con movimiento, color y tamaño")

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (23, 157, 255)

# Rectángulos
rect1 = pygame.Rect(800, 100, 100, 50)   # rojo
rect2 = pygame.Rect(800, 800, 100, 50)   # azul

# Configuración
cambio = 1
SIZE_STEP = 10   # cuanto crece o disminuye rect1 por pulsación

# Reloj
reloj = pygame.time.Clock()
FPS = 120

while QUIERO_SEGUIR_JUGANDO:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()

    # ---- Movimiento rect1 (rojo) ----
    if teclas[pygame.K_a] and rect1.x > 0:
        rect1.x -= cambio
    if teclas[pygame.K_d] and rect1.x + rect1.w < ANCHO:
        rect1.x += cambio
    if teclas[pygame.K_w] and rect1.y > 0:
        rect1.y -= cambio
    if teclas[pygame.K_s] and rect1.y + rect1.h < ALTO:
        rect1.y += cambio

    # ---- Movimiento rect2 (azul) ----
    if teclas[pygame.K_LEFT] and rect2.x > 0:
        rect2.x -= cambio
    if teclas[pygame.K_RIGHT] and rect2.x + rect2.w < ANCHO:
        rect2.x += cambio
    if teclas[pygame.K_UP] and rect2.y > 0:
        rect2.y -= cambio
    if teclas[pygame.K_DOWN] and rect2.y + rect2.h < ALTO:
        rect2.y += cambio

    # ---- Cambiar color con tecla C ----
    if teclas[pygame.K_c]:
        ROJO = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        AZUL = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    # ---- Aumentar tamaño de rect1 (rojo) con T ----
    if teclas[pygame.K_t]:
        new_width  = rect1.width  + SIZE_STEP
        new_height = rect1.height + SIZE_STEP

        # Limitar para que NO salga de la ventana
        if rect1.x + new_width <= ANCHO and rect1.y + new_height <= ALTO:
            rect1.width  = new_width
            rect1.height = new_height

    # ---- Disminuir tamaño de rect1 con Y ----
    if teclas[pygame.K_y]:
        new_width  = rect1.width  - SIZE_STEP
        new_height = rect1.height - SIZE_STEP

        if new_width > 10 and new_height > 10:
            rect1.width  = new_width
            rect1.height = new_height
        # ---- Cambiar velocidad con + y - ----
    if teclas[pygame.K_PLUS] or teclas[pygame.K_KP_PLUS]:   # teclado normal y numérico
        if cambio < 20:   # límite máximo opcional
            cambio += 1

    if teclas[pygame.K_MINUS] or teclas[pygame.K_KP_MINUS]:
        if cambio > 1:    # no bajar a cero
            cambio -= 1
    
    rect1.colliderect(rect2)

        # ---- Detección de colisión ----
    if rect1.colliderect(rect2):
        ROJO = (255, 0, 255)   # rect1 cambia a rosa
        AZUL = (0, 200, 200)   # rect2 cambia a turquesa
    else:
        ROJO = (255, 0, 0)     # vuelve a rojo si no hay contacto
        AZUL = (23, 157, 255)  # vuelve a azul si no hay contacto

    







    # Dibujar
    ventana.fill(BLANCO)
    pygame.draw.rect(ventana, ROJO, rect1)
    pygame.draw.rect(ventana, AZUL, rect2)
    pygame.display.flip()

    reloj.tick(FPS)

