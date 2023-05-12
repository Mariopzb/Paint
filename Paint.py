"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
"""
from turtle import *

from freegames import vector
def line(start, end):
    """Dibuja una linea dada 2 puntos dados. Start es el primer clic y end el segundo"""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)
    
def square(start, end, color):
    """Dibuja un cuadrado teniendo el inicio y final, ademas del color"""
    up()
    goto(start.x, start.y)
    down()
    color(color)
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

"usando la funcion onkey de turtle para asignar colores a las teclas"
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('pink'), 'P')

def circle(start, end, color):
    """Dibuja un circulo con el color dado."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(360):
        forward(2)
        left(1)

    end_fill()
    
def rectangle(start, end, color):
    """Es la misma que la del cuadrado solo que a esta se le agregan 2 medidas
      para obtener el alto y ancho"""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()
    

def triangle(start, end, color):
    """Dibuja un triangulo, con la misma funcion del cuadrado solo cambia el angulo"""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(60)

    end_fill()

def tap(x, y):
    """Guarda el punto inicial para comenzar el dibujo, si no se ha declarado ninguno entonces start=none.
    Si hay algun punto, entonces la funcion almacenara un punto end para determinar hasta donde quedara dibujada la forma
    """
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    """
    Almacena un valor en una estructura de datos, para despues poder acceder a el utilzando su clave(key) correspondiente
    """
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
#Las letras en mayusculas son usadas para elegir el color de la forma
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('pink'), 'P')
#Las letras en minuscula son usadas para escoger la forma a dibujar
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
