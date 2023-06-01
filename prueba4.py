"""codigo en python para el paint en comandos"""
# pylint: disable=C0103
# pylint: disable=E1101
import math
import pygame

class Paint:
    """class paint es para el programa paint donde se dibuja en este caso por comandos"""
    def __init__(self, ancho, alto):
        pygame.init()
        self.superficie = pygame.display.set_mode((ancho, alto))
        self.color_fondo = (0, 0, 0)
        self.color = (255, 0, 0)

    def dibujar_linea_horizontal(self, ejex, ejey, longitud):
        """funcion para dibujar una línea horizontal"""
        for i in range(longitud):
            self.superficie.set_at((ejex + i, ejey), self.color)
        pygame.display.flip()

    def dibujar_linea_vertical(self, ejex, ejey, longitud):
        """funcion para dibujar una línea vertical"""
        for i in range(longitud):
            self.superficie.set_at((ejex, ejey + i), self.color)
        pygame.display.flip()

    def dibujar_rectangulo(self, ex, ey, ancho, alto):
        """funcion para dibujar un rectángulo"""
        self.dibujar_linea_horizontal(ex, ey, ancho)
        self.dibujar_linea_vertical(ex, ey, alto)
        self.dibujar_linea_horizontal(ex, ey + alto, ancho)
        self.dibujar_linea_vertical(ex + ancho, ey, alto)

    def dibujar_cuadrado(self, x, y, lado):
        """funcion para dibujar un cuadrado"""
        for i in range(lado):
            for j in range(lado):
                self.superficie.set_at((x + i, y + j), self.color)
        pygame.display.flip()

    def dibujar_circulo(self, x_centro, y_centro, radio):
        """funcion para dibujar un círculo"""
        for ejex in range(x_centro - radio, x_centro + radio + 1):
            for ejey in range(y_centro - radio, y_centro + radio + 1):
                distancia = math.sqrt((ejex - x_centro) ** 2 + (ejey - y_centro) ** 2)
                if distancia <= radio:
                    self.superficie.set_at((ejex, ejey), self.color)
        pygame.display.flip()

    def dibujar_triangulo_equilatero(self, x, y, lado):
        """funcion para dibujar un triángulo equilátero"""
        altura = lado * math.sqrt(3) / 2
        x1 = int(x)
        y1 = int(y + altura)
        x2 = int(x - lado / 2)
        y2 = int(y)
        x3 = int(x + lado / 2)
        y3 = int(y)

        self.dibujar_linea(x1, y1, x2, y2)
        self.dibujar_linea(x2, y2, x3, y3)
        self.dibujar_linea(x3, y3, x1, y1)

    def dibujar_triangulo_escaleno(self, x1, y1, x2, y2, x3, y3):
        """funcion para dibujar un triángulo escaleno"""
        self.dibujar_linea(x1, y1, x2, y2)
        self.dibujar_linea(x2, y2, x3, y3)
        self.dibujar_linea(x3, y3, x1, y1)

    def dibujar_triangulo_isosceles(self, x, y, base, altura):
        """funcion para dibujar un triángulo isósceles"""
        x1 = int(x)
        y1 = int(y)
        x2 = int(x - base / 2)
        y2 = int(y + altura)
        x3 = int(x + base / 2)
        y3 = int(y + altura)

        self.dibujar_linea(x1, y1, x2, y2)
        self.dibujar_linea(x2, y2, x3, y3)
        self.dibujar_linea(x3, y3, x1, y1)

    def dibujar_linea(self, x1, y1, x2, y2):
        """funcion para dibujar una línea de los triangulos"""
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = -1 if x1 > x2 else 1
        sy = -1 if y1 > y2 else 1
        err = dx - dy

        while x1 != x2 or y1 != y2:
            self.superficie.set_at((int(x1), int(y1)), self.color)
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

        pygame.display.flip()

    def run(self):
        """bucle principal"""
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()


if __name__ == '__main__':
    paint = Paint(800, 600)
    with open("comandos.cmd.txt", "r", encoding="utf-8") as myfile:
        for linea in myfile:
            linea = linea.strip().split()
            comando = linea[0]

            if comando == "exit":
                pygame.quit()
            elif comando == "fondo":
                if len(linea) >= 4:
                    r = int(linea[1])
                    g = int(linea[2])
                    b = int(linea[3])
                    paint.color_fondo = (r, g, b)
                    paint.superficie.fill(paint.color_fondo)
            elif comando == "linea":
                direccion = linea[1]
                ejx = int(linea[2])
                ejy = int(linea[3])
                longitudd = int(linea[4])

                if direccion == "-h":
                    paint.dibujar_linea_horizontal(ejx, ejy, longitudd)
                elif direccion == "-v":
                    paint.dibujar_linea_vertical(ejx, ejy, longitudd)
            elif comando == "circulo":
                if len(linea) >= 4:
                    ejex_centro = int(linea[1])
                    ejey_centro = int(linea[2])
                    radioo = int(linea[3])
                    paint.dibujar_circulo(ejex_centro, ejey_centro, radioo)
            elif comando == "triangulo":
                if len(linea) >= 4:
                    tipo = linea[1]
                    if tipo == "equilatero":
                        ejx = float(linea[2])
                        ejy = float(linea[3])
                        ladoo = float(linea[4])
                        paint.dibujar_triangulo_equilatero(ejx, ejy, ladoo)
                    elif tipo == "escaleno":
                        ex1 = float(linea[2])
                        ey1 = float(linea[3])
                        ex2 = float(linea[4])
                        ey2 = float(linea[5])
                        ex3 = float(linea[6])
                        ey3 = float(linea[7])
                        paint.dibujar_triangulo_escaleno(ex1, ey1, ex2, ey2, ex3, ey3)
                    elif tipo == "isosceles":
                        ejx = float(linea[2])
                        ejy = float(linea[3])
                        basee = float(linea[4])
                        alturaa = float(linea[5])
                        paint.dibujar_triangulo_isosceles(ejx, ejy, basee, alturaa)
            elif comando == "cuadrado":
                if len(linea) >= 4:
                    ejx = int(linea[1])
                    ejy = int(linea[2])
                    ladoo = int(linea[3])
                    paint.dibujar_cuadrado(ejx, ejy, ladoo)
            elif comando == "rectangulo":
                if len(linea) >= 5:
                    ejx = int(linea[1])
                    ejy = int(linea[2])
                    anchoo = int(linea[3])
                    altoo = int(linea[4])
                    paint.dibujar_rectangulo(ejx, ejy, anchoo, altoo)
if __name__ == "__main__":
    ancho_pantalla = 800
    alto_pantalla = 600

    programa = Paint(ancho_pantalla, alto_pantalla)
    programa.ejecutar_comandos("comandos.cmd.txt")
