import pygame
import sys
import math

# Inicializar pygame
pygame.init()

# Definir colores
blanco = (255, 255, 255)
rojo = (255, 0, 0)
verde = (0, 255, 0)

# Definir dimensiones de la pantalla
ancho = 800
alto = 600

# Crear la pantalla
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Colisión elástica de Bolas")

# Definir las bolas
class Bola(pygame.sprite.Sprite):
    def __init__(self, color, radio, x, y, vel_x, vel_y):
        super().__init__()
        self.image = pygame.Surface([radio*2, radio*2])
        self.image.fill(blanco)
        pygame.draw.circle(self.image, color, (radio, radio), radio)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y

bola1 = Bola(rojo, 20, 100, 300, 3, 0)
bola2 = Bola(verde, 20, 600, 300, -3, 0)

# Crear un grupo para las bolas
bolas = pygame.sprite.Group()
bolas.add(bola1, bola2)

# Bucle principal del juego
jugando = True
reloj = pygame.time.Clock()
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Actualizar la posición de las bolas
    bola1.rect.x += bola1.vel_x
    bola1.rect.y += bola1.vel_y
    bola2.rect.x += bola2.vel_x
    bola2.rect.y += bola2.vel_y

    # Verificar colisión con los bordes de la pantalla
    if bola1.rect.left < 0 or bola1.rect.right > ancho:
        bola1.vel_x *= -1
    if bola1.rect.top < 0 or bola1.rect.bottom > alto:
        bola1.vel_y *= -1
    if bola2.rect.left < 0 or bola2.rect.right > ancho:
        bola2.vel_x *= -1
    if bola2.rect.top < 0 or bola2.rect.bottom > alto:
        bola2.vel_y *= -1

    # Verificar colisión entre las bolas
    distancia = math.sqrt((bola1.rect.x - bola2.rect.x)**2 + (bola1.rect.y - bola2.rect.y)**2)
    if distancia <= bola1.rect.width + bola2.rect.width:
        # Calcular nueva velocidad después de la colisión elástica
        v1x = ((bola1.vel_x * (bola1.rect.width - bola2.rect.width)) + (2 * bola2.rect.width * bola2.vel_x)) / (bola1.rect.width + bola2.rect.width)
        v1y = ((bola1.vel_y * (bola1.rect.width - bola2.rect.width)) + (2 * bola2.rect.width * bola2.vel_y)) / (bola1.rect.width + bola2.rect.width)
        v2x = ((bola2.vel_x * (bola2.rect.width - bola1.rect.width)) + (2 * bola1.rect.width * bola1.vel_x)) / (bola1.rect.width + bola2.rect.width)
        v2y = ((bola2.vel_y * (bola2.rect.width - bola1.rect.width)) + (2 * bola1.rect.width * bola1.vel_y)) / (bola1.rect.width + bola2.rect.width)

        bola1.vel_x = v1x
        bola1.vel_y = v1y
        bola2.vel_x = v2x
        bola2.vel_y = v2y

    # Limpiar la pantalla
    pantalla.fill(blanco)

    # Dibujar las bolas en la pantalla
    bolas.draw(pantalla)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    reloj.tick(60)

# Salir del juego
pygame.quit()
sys.exit()

## Hecho con ayuda de video de youtube