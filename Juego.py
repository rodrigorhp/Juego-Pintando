#Rodrigo Henriquez A00827198
#Luis Angel Mendoza A00827838


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
import turtle
import math

#Funcion para dibujar una linea
def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

#funcion para dibujar un cuadrado
def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

#funcion para dibujar un cuadrado
def circle(start, end):
    "Draw circle from start to end."
    t = turtle.Turtle()

    t.penup()
    t.setposition(start.x,start.y)
    t.down()
    begin_fill()
    p1 = [start.x, start.y]
    p2 = [end.x, end.y]
    r = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )/2
    t.circle(r) 
    end_fill()
#funcion para dibujar un rectangulo
def rectangle(start, end):
    "Draw rectangle from start to end."
    pass  # TODO

#funcion para dibujar un triangulo
def triangle(start, end):
    "Draw triangle from start to end."
    pass  # TODO

#Funcion para guardar las posiciones de los clicks
def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

#funcion para determinar la forma
def store(key, value):
    "Store value in state at key."
    state[key] = value

#Inicializa los valores de las figuras, colores y los clicks 
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
# Añadir un color
onkey(lambda:color ('yellow'), 'Y')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
