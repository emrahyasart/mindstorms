import turtle

def draw_square(some_turtle):
    for i in range (0,4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(20)

    for i in range(1,37):
        draw_square(brad)
        brad.right(10)

def angie_and_dady():
    window = turtle.Screen()
    window.bgcolor("magenta")

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    dady = turtle.Turtle()
    dady.shape("turtle")
    dady.color("green")
    dady.speed(3)

    i = 0
    while i < 3:
        dady.forward(100)
        dady.right(120)
        i += 1

    window.exitonclick()


draw_art()

angie_and_dady()