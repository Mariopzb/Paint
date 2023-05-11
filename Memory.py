from random import *
from turtle import *
from freegames import path

#Se importa una imagen de la galeria de gif
car = path('car.gif')

#Como metodo de innovación se decidieron agregar símbolos y emojis en vez de numeros
#Si son hechos con numeros simplemtente se hace un list(range(36)) o dependiendo del numero de fichas que sean
tiles = ["\u267f", "\u260e", "\100", "\u262f", "\u2718", 
         "\u2605", "\u2603","\u0bf9", "\u2702", "\u2716",
         "\u20b1", "\u266c", "\uffe6", "\u273f", "\u2601", 
         "\u2744", "\u2728", "\u0e3f", "\u20b7", "\u2654", 
         "\u2655", "\u2656", "\u2657", "\u2658", "\u2659", 
         "\u265a", "\u265b", "\u265c", "\u265d", "\u265e", 
         "\u265f", "\u26bd"] * 2
state = {'mark': None}
hide = [True] * 64
taps = {"number_taps": 0}
writer = Turtle(visible=False)

#Se dibuja el area de juego en un punto especifico y esta esta llena de cuadrados, esta recibe coordenadas x, y
def square(x, y):
    "Dibuja un cuadro blanco con contorno negro (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Se utiliza para encontrar una casilla en especifica en un tablero dadas las cordenadas xy"
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Se usa para mapear un indice de una casilla donde se puede dibujar un objeto o forma similar"
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Marca la ficha tocada por el usuario y si esta es igual que la anterior se revelan ambas fichas, recibe coordenadas x, y"
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
#Empieza el conteo del numero de taps
    taps["number_taps"] += 1n

def draw():
    "Esta funcion actualiza la pantalla cada que el usuario realiza alguna accion, recorre las 64 fichas y comprueba que esten ocultas"
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
         #Aqui se centran los digítos, en caso de tener simbolos no es necesario, ya que ocupan la mayoría del cuadro
        """if tiles[mark] >= 10:
            goto(x + 3, y)
        else:
            goto(x + 5,y)"""
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))
    
#Aqui se agregan los numeros de taps a la pantalla
    writer.clear()
    writer.goto(250, 115)
    style = ('Arial', 20, 'italic')
    writer.pendown()
    writer.write('Taps: ' + str(taps["number_taps"]), font=style, align='center')

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
