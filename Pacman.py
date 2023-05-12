from random import choice
from turtle import *
from freegames import floor, vector

state = {'score': 0}
path = Turtle(visible=False)
writer = Turtle(visible=False)
aim = vector(5, 0)
pacman = vector(-40, -80)
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]
#Crea una matriz de 20x20, en la que los 0 son areas en negro donde no se puede avanzar y los 1 son casillas donde si.
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

def square(x, y):
    "Se dibuja un cuadrado que sera el tablero del juego dadas por las coordenadas x, y"
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

def offset(point):
    "El argumento pedido por la funcion es point, calcula el indice de un punto en nuestra cuadricula de 20x20"
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

#En esta funcion se verifica que la posicion de los fantasmas y el pacman sea valida
def valid(point):
    
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0

#En esta funcion se dibuja el mapa del mundo y cada cuadro en el, si este cuadro es igual a 1 entonces tendra un punto dentro
def world():
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')

def move():     #Se define como se mueve el pacman y los fantasmas
    "Move pacman and all ghosts."
    writer.undo()
    writer.write(state['score'])

    clear()

    if valid(pacman + aim):     #Revisa si el pacman se puede mover en la direccion a la que esta viendo
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:       #Revisa si el pacman a obtenido un punto
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    for point, course in ghosts:        #Se encarga del movimiento de los fantasmas
        if valid(point + course):       #Evita que los fantasmas colisionen con las paredes
            point.move(course)
        else:                           #Al quedarse sin camino empezara a correr esta parte 
            #Los fantasmas seran un poco mas inteligentes, estos trataran de acercarse al pacman para hacerlo mas dificil
            if pacman.x > point.x and pacman.y > point.y:
                options = [
                vector(10, 0),
                vector(10, 0),
                vector(10, 0),
                vector(-10, 0),
                vector(0, 10),
                vector(0, 10),
                vector(0, 10),
                vector(0, -10),
            ]
            elif pacman.x < point.x and pacman.y > point.y:
                options = [
                vector(10, 0),
                vector(-10, 0),
                vector(-10, 0),
                vector(-10, 0),
                vector(0, 10),
                vector(0, 10),
                vector(0, 10),
                vector(0, -10),
            ]
            elif pacman.x > point.x and pacman.y < point.y:
                options = [
                vector(10, 0),
                vector(10, 0),
                vector(10, 0),
                vector(-10, 0),
                vector(0, 10),
                vector(0, -10),
                vector(0, -10),
                vector(0, -10),
            ]
            elif pacman.x < point.x and pacman.y < point.y:
                options = [
                vector(10, 0),
                vector(-10, 0),
                vector(-10, 0),
                vector(-10, 0),
                vector(0, 10),
                vector(0, -10),
                vector(0, -10),
                vector(0, -10),
            ]
            else:
                options = [         #Este else es en caso de que se encuentren en un punto en comun, dar oportunidad al jugador de no ser perseguido
                vector(10, 0),
                vector(-10, 0),
                vector(0, 10),
                vector(0, -10),
                ]

            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')

    update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    ontimer(move, 30)

    #Actualiza la dirección en la que se mueve el pacman. Buscando si la direccion es valida
def change(x, y):
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()
