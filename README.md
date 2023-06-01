##Paint Program
#Este es un programa de dibujo en Python que permite dibujar formas como líneas, rectángulos, círculos y triángulos utilizando comandos.

Requisitos
Python 3.x
Pygame (puedes instalarlo con pip install pygame)
Uso
Descarga o clona este repositorio en tu máquina local.
Asegúrate de tener Python 3.x instalado.
Instala la biblioteca Pygame ejecutando el siguiente comando en tu terminal:
pip install pygame
Ejecuta el programa con el siguiente comando:
python paintfinal.py
El programa abrirá una ventana de visualización donde podrás dibujar utilizando comandos.
Los comandos están definidos en el archivo "comandos.cmd.txt". Puedes editar ese archivo para personalizar los dibujos que se mostrarán en la ventana.
#Comandos
Los comandos se definen en el archivo "comandos.cmd.txt" y se ejecutan secuencialmente. Cada línea del archivo representa un comando y sus parámetros separados por espacios.

Comando "exit": Cierra el programa.
Comando "fondo r g b": Establece el color de fondo de la ventana utilizando los valores RGB.
Comando "linea -h ejex ejey longitud": Dibuja una línea horizontal.
Comando "linea -v ejex ejey longitud": Dibuja una línea vertical.
Comando "circulo ejex_centro ejey_centro radio": Dibuja un círculo.
Comando "triangulo equilatero ejx ejy lado": Dibuja un triángulo equilátero.
Comando "triangulo escaleno ex1 ey1 ex2 ey2 ex3 ey3": Dibuja un triángulo escaleno.
Comando "triangulo isosceles ejx ejy base altura": Dibuja un triángulo isósceles.
Comando "cuadrado ejx ejy lado": Dibuja un cuadrado.
Comando "rectangulo ejx ejy ancho alto": Dibuja un rectángulo.