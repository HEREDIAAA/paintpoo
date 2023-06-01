import pygame
import math

# Inicializar Pygame
pygame.init()

# Crear una superficie de 800x600 píxeles
ancho = 800
alto = 600
superficie = pygame.display.set_mode((ancho, alto))

# Establecer el color predeterminado a rojo (255, 0, 0)
color = (255, 0, 0)

def dibujar_linea_horizontal(x, y, longitud):
    for i in range(longitud):
        superficie.set_at((x + i, y), color)
    pygame.display.flip()

def dibujar_linea_vertical(x, y, longitud):
    for i in range(longitud):
        superficie.set_at((x, y + i), color)
    pygame.display.flip()

def dibujar_circulo(x_centro, y_centro, radio):
    for x in range(x_centro - radio, x_centro + radio + 1):
        for y in range(y_centro - radio, y_centro + radio + 1):
            distancia = math.sqrt((x - x_centro) ** 2 + (y - y_centro) ** 2)
            if distancia <= radio:
                superficie.set_at((x, y), color)
    pygame.display.flip()

myfile = open("comandos.cmd", "r", encoding="utf-8")

for linea in myfile:
    linea = linea.strip().split()
    comando = linea[0]

    if comando == "exit":
        pygame.quit()
    elif comando == "color":
        if len(linea) >= 4:  # Verificar que la línea tenga suficientes elementos
            r = int(linea[1])
            g = int(linea[2])
            b = int(linea[3])
            color = (r, g, b)
    elif comando == "linea":
        direccion = linea[1]
        x = int(linea[2])
        y = int(linea[3])
        longitud = int(linea[4])

        if direccion == "-h":
            dibujar_linea_horizontal(x, y, longitud)
        elif direccion == "-v":
            dibujar_linea_vertical(x, y, longitud)
    elif comando == "circulo":
        if len(linea) >= 4:  # Verificar que la línea tenga suficientes elementos
            x_centro = int(linea[1])
            y_centro = int(linea[2])
            radio = int(linea[3])
            dibujar_circulo(x_centro, y_centro, radio)

myfile.close()

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
