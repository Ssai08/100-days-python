from turtle import Turtle,Screen
from xmlrpc.client import FastParser

tim = Turtle()
sc = Screen()

sc.screensize(600,600,"black")
sc.tracer(0)

tim.hideturtle()
tim.color("white")
tim.penup()
tim.goto(0,300)
tim.write("Score: ",False,"center",('Arial', 11, 'normal'))
# tim.write("Hello")

sc.update()
sc.exitonclick()