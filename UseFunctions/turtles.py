
import turtle

def draw_square(t):

    for _ in range(4):
        t.fd(100)
        t.rt(90)


def draw_circle(t):

    t.circle(50)


def draw_triangle(t):

    for _ in range(3):
        t.fd(100)
        t.rt(120)


def draw_hallows(t):

    for _ in range(3):
        t.fd(300)
        t.lt(120)

    t.fd(150)
    t.circle(87)

    t.lt(90)
    t.fd(250)

def draw_art():
    window = turtle.Screen()
    window.bgcolor('blue')

    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('green')
    brad.speed(3)

    # draw_square(brad)
    # draw_circle(brad)
    # draw_triangle(brad)
    draw_hallows(brad)

    window.exitonclick()


draw_art()