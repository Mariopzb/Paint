
#Juego de la Víbora (Snake)

from turtle import *
from random import randrange
from freegames import square, vector

#Declaración de variables.
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
color1 = random.randint(1, 5)
color2 = random.randint(1, 5)

#Asigna al azar 5 posibles colores a las variables "color1" y "color2".
if color1 != color2:
    if color1 == 1:
        color1 = 'blue'
    if color1 == 2:
        color1 = 'orange'
    if color1 == 3:
        color1 = 'green'
    if color1 == 4:
        color1 = 'yellow'
    if color1 == 5:
        color1 = 'pink'
    
    if color2 == 1:
        color2 = 'blue'
    if color2 == 2:
        color2 = 'orange'
    if color2 == 3:
        color2 = 'green'
    if color2 == 4:
        color2 = 'yellow'
    if color2 == 5:
        color2 = 'pink'
else:
    #Si los colores llegan a conicidir, asina un color predeterminado a cada variable para evitar que sean iguales.
    color1 = "black"
    color2 = "blue"


def change(x, y):
    #Determinar y cambiar la dirección en la que se va a mover la serpiente.
    aim.x = x
    aim.y = y

def inside(head):
    #Indica si la cabeza de la serpiente está dentro del límite del espacio del juego.
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    #Limita a la serpiente a moverse solo en "x" y "y" (derecha, izquierda, arriba, abajo).
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        #Cuando la cabeza de la serpiente toca algun borde del espacio, el juego termina y la cabeza se pondrá en rojo.
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        #Mueve un paso a la vez la "comida"; si la serpiente logra alcanzar la comida crece, sino se queda con su tamaño original.
        print('Snake:', len(snake))
        food.x = randrange(-1, 1) * 10
        food.y = randrange(-1, 1) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        #La variable "color1" se coloca para que la serpiente cambie de color en cada partida.
        square(body.x, body.y, 9, color1)

    square(food.x, food.y, 9, color2) #Se coloca la variable "color2" para que la comida cambie de color en cada partida
    update()
    ontimer(move, 100) #Cambia la velocidad en que se mueve la serpiente.

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
