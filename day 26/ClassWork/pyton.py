from turtle import *
def walk():
    forward(200)
    left(90)

def fall_back():
    left(90)
    forward(200)
def walk_fall_back():
    walk()
    fall_back()
walk()
fall_back()



exitonclick()

