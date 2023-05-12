#Juego de tiro parabólico (Cannon)

from random import randrange
from turtle import *
from freegames import vector

#Declaración de variables.
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Respond to screen tap."
    #Delimita el espacio del juego en donde estará el proyectil; además, determina la velocidad del proyectil.
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 20
        speed.y = (y + 200) / 20

def inside(xy):
    #Delimita el espacio del juego. 
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    #Dibuja puntos de dos dimensiones y colores distintintos; los posiciona en lugares específicos.
    clear()

    for target in targets:
        "For para los balones, crea círculos de tamaño 20 y color azul."
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        "If para el proyectil, crea círculos de tamaño 6 y color rojo."
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    """Move ball and targets."""
    #Determina la posición y dirección de movimiento tanto del proyectil como de los balones.
    "Balones"
    if len(targets) < max_targets:
        #Genera un nuevo balón en una posición aleatoria.
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5
        if not inside(target):
           #Reposiciona los balones en una posición aleatoria.
            targets.remove(target)
            y = randrange(-150, 150)
            target.x = 200
            target.y = y
            targets.append(target)
    "Proyectil"
    if inside(ball):
       #Indica la velocidad a la que se moverá en el eje "y" el proyectil.
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        #Indica la cantidad de balones que van a ir saliendo en el juego. 
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    ontimer(move, 25) #Determina la velocidad de los balones.

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
