"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""
from turtle import *

from freegames import vector
def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)
    
def square(start, end, color):
    """Draw square from start to end with given color."""
    up()
    goto(start.x, start.y)
    down()
    color(color)
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

"usando la fucnion onkey de turtle para asignar colores a las teclas"
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')

def circle(start, end, color):
    """Dibuja un circulo con el color dado."""
    up()
    goto(start.x, start.y)
    down()
    color(color)
    begin_fill()

    radius = (end - start).mag()
    circle(radius)

    end_fill()

def rectangle(start, end, color):
    """Es la misma que la del cuadrado solo que a esta se le agregan 2 medidas
      para obtener el alto y ancho"""
    up()
    goto(start.x, start.y)
    down()
    color(color)
    begin_fill()

    width = end.x - start.x
    height = end.y - start.y

    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)

    end_fill()
    

def triangle(start, end, color):
    """Dibuja un triangulo"""
    up()
    goto(start.x, start.y)
    down()
    color(color)
    begin_fill()

    goto(end.x, end.y)
    goto(start.x + (end.x - start.x) / 2, start.y + (end.y - start.y))
    goto(start.x, start.y)

    end_fill()

def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
