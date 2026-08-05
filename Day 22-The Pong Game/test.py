import turtle as t

self.penup()
self.goto(0, 500)  # Start position
self.setheading(270)
self.pendown()
for _ in range(20):  # 20 dots
    self.forward(10)   # Draw small line (dot effect)
    self.penup()
    self.forward(10)   # Gap between dots
    self.pendown()

# self.done()
