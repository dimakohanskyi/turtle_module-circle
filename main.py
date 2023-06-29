import turtle
from turtle import Turtle, Screen
import random


tim = Turtle()


turtle.colormode(255)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


def draw_spiro(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.circle(100)
        tim.color(random_colour())
        tim.setheading(tim.heading() + size_of_gap)
        tim.speed(50)


draw_spiro(5)

screen = Screen()
screen.exitonclick()