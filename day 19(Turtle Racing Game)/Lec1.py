import turtle as t

tim = t.Turtle()
sc = t.Screen()
sc.listen()

def move_forward():
    tim.fd(10)
def move_backward():
    tim.bk(10)
def turn_left():
    tim.left(5)
def turn_right():
    tim.right(5)
def clear():
    tim.reset()
    # tim.speed(0)
    # tim.home()
    # tim.clear()

sc.onkeypress(move_forward,"w")
sc.onkeypress(move_backward,"s")
sc.onkeypress(turn_right,"d")
sc.onkeypress(turn_left,"a")
sc.onkeypress(clear,"c")
# tim.fd(100)

sc.exitonclick()
