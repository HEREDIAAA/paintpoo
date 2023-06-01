import pygame
import math

# Inicializar Pygame
pygame.init()

# Crear una superficie de 800x600 píxeles
ancho = 800
alto = 600
superficie = pygame.display.set_mode((ancho, alto))

# Establecer el color de fondo predeterminado a negro (0, 0, 0)
color_fondo = (0, 0, 0)

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

def dibujar_triangulo_equilatero(x, y, lado):
    altura = lado * math.sqrt(3) / 2
    x1 = int(x)
    y1 = int(y + altura)
    x2 = int(x - lado / 2)
    y2 = int(y)
    x3 = int(x + lado / 2)
    y3 = int(y)

    dibujar_linea(x1, y1, x2, y2)
    dibujar_linea(x2, y2, x3, y3)
    dibujar_linea(x3, y3, x1, y1)

def dibujar_linea(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = -1 if x1 > x2 else 1
    sy = -1 if y1 > y2 else 1
    err = dx - dy

    while x1 != x2 or y1 != y2:
        superficie.set_at((int(x1), int(y1)), color)
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

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
    elif comando == "fondo":
        if len(linea) >= 4:  # Verificar que la línea tenga suficientes elementos
            r = int(linea[1])
            g = int(linea[2])
            b = int(linea[3])
            color_fondo = (r, g, b)
            superficie.fill(color_fondo)
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
    elif comando == "triangulo":
        if len(linea) >= 4:  # Verificar que la línea tenga suficientes elementos
            x = float(linea[1])
            y = float(linea[2])
            lado = float(linea[3])
            dibujar_triangulo_equilatero(x, y, lado)

myfile.close()

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

