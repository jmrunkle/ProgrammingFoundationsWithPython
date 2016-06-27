
import turtle
from traceback import print_stack

def draw_square(t):

    for _ in range(4):
        t.fd(100)
        t.rt(90)


def draw_circle(t):

    t.circle(50)


def draw_triangle(t, size):

    for _ in range(3):
        t.fd(size)
        t.rt(120)


def draw_hallows(t):

    for _ in range(3):
        t.fd(300)
        t.lt(120)

    t.fd(150)
    t.circle(87)

    t.lt(90)
    t.fd(250)

# def draw_art():
#     window = turtle.Screen()
#     window.bgcolor('blue')

#     brad = turtle.Turtle()
#     brad.shape('turtle')
#     brad.color('green')
#     brad.speed(3)

#     # draw_square(brad)
#     # draw_circle(brad)
#     # draw_triangle(brad, 100)
#     draw_hallows(brad)

#     window.exitonclick()

def draw_fractal_triangle(t, size):
    draw_triangle(t, size)
    if size < 4:
        return
    size = size // 2
    draw_fractal_triangle(t, size)
    t.fd(size)
    draw_fractal_triangle(t, size)
    t.rt(60)
    t.fd(size)
    t.rt(60)
    draw_fractal_triangle(t, size)
    t.rt(60)
    t.fd(size)
    t.rt(60)
    t.fd(size)
    t.rt(120)


def draw_fractal():
    window = turtle.Screen()
    window.bgcolor('blue')

    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('green')
    brad.speed(11)

    brad.pu()
    brad.setx(-128)
    brad.sety(-110)
    brad.seth(60)

    brad.pd()
    draw_fractal_triangle(brad, 256)

    window.exitonclick()


# draw_art()
draw_fractal()