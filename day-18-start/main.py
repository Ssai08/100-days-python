from subprocess import check_output
import turtle as t
import colorgram as c
from random import choice, randint

timmy = t.Turtle()
timmy.speed(0)
t.colormode(255)
timmy.pensize(20)
timmy.teleport(-150,150)
timmy.penup()

def random_colour():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    random_color = (r, g, b)
    return random_color


# def extract_colours():
#     colors = c.extract('download.jpeg',20)
#     color_list = []
#
#     for color_combo in colors:
#         temp_list = []
#         for value in color_combo.rgb:
#             temp_list.append(value)
#         color_list.append(tuple(temp_list))
#     return color_list

# color_list = extract_colours()


# timmy.setheading(90)
# timmy.forward(100)

def print_one_line(count):
    x = timmy.xcor()
    y = timmy.ycor()
    for i in range(count):
        colour = random_colour()
        timmy.color(colour)
        timmy.dot()
        timmy.forward(50)
    timmy.teleport(x,y-50)


for i in range(10):
    print_one_line(10)

timmy.hideturtle()

# timmy.dot()
sc = t.Screen()
sc.exitonclick()





# def spirograph(angel):
#     timmy.circle(100)
#     timmy.left(angel)
#     while timmy.heading()!=0:
#         timmy.color(random_colour())
#         timmy.circle(100)
#         timmy.left(angel)
#
# spirograph(5)


##########################*************************************######################################
# def random_walk(num_steps):
#     for i in range(num_steps):
#         # timmy.color(choice(colors))
#         timmy.color(random_colour())
#         timmy.forward(20)
#         timmy.left(choice(direction))
#
#
# def random_colour():
#     r = randint(0,255)
#     g = randint(0,255)
#     b = randint(0,255)
#     random_color = (r, g, b)
#     return random_color
#
#
# timmy.speed(11)
# timmy.pensize(5)
# direction = [0,90,180,270]
#
# random_walk(500)




##########################*************************************######################################

# timmy.shape("square")

# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)

#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()


# for i in range(15):
#     timmy.color("black")
#     timmy.forward(10)
#     timmy.color("white")
#     timmy.forward(10)
colors = [
    "alice blue", "antique white", "aquamarine", "azure", "bisque", "blanched almond", "blue violet", "burlywood",
    "cadet blue", "chartreuse", "coral", "cornflower blue", "crimson", "dark blue", "dark cyan", "dark goldenrod",
    "dark gray", "dark green", "dark khaki", "dark magenta", "dark olive green", "dark orange", "dark orchid",
    "dark red", "dark salmon", "dark sea green", "dark slate blue", "dark slate gray", "dark turquoise",
    "dark violet", "deep pink", "deep sky blue", "dim gray", "dodger blue", "firebrick", "floral white",
    "forest green", "fuchsia", "gainsboro", "ghost white", "goldenrod", "green yellow", "honeydew", "hot pink",
    "indian red", "ivory", "khaki", "lavender", "lavender blush", "lawn green", "lemon chiffon", "light blue",
    "light coral", "light cyan", "light goldenrod yellow", "light gray", "light green", "light pink",
    "light salmon", "light sea green", "light sky blue", "light slate gray", "light steel blue", "light yellow",
    "lime", "lime green", "linen", "medium aquamarine", "medium blue", "medium orchid", "medium purple",
    "medium sea green", "medium slate blue", "medium spring green", "medium turquoise", "medium violet red",
    "midnight blue", "mint cream", "misty rose", "moccasin", "navajo white", "old lace", "olive", "olive drab",
    "orange red", "orchid", "pale goldenrod", "pale green", "pale turquoise", "pale violet red", "papaya whip",
    "peach puff", "peru", "plum", "powder blue", "rosy brown", "royal blue", "saddle brown", "salmon",
    "sandy brown", "sea green", "seashell", "sienna", "silver", "sky blue", "slate blue", "slate gray", "snow",
    "spring green", "steel blue", "tan", "thistle", "tomato", "turquoise", "violet red", "wheat", "yellow green"
]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for j in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
# timmy.penup()
# timmy.left(90)
# timmy.forward(300)
# timmy.right(90)
# timmy.pendown()
# for sides in range(3,11):
#     timmy.color(choice(colors))
#     draw_shape(sides)

## DRAW A STAR
# while True:
#     timmy.forward(200)
#     timmy.left(170)
#     if abs(timmy.pos()) < 1:
#         break