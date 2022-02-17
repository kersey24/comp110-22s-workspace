"""Turtle tutorial."""

from turtle import Turtle, colormode, done 
leo: Turtle = Turtle()

colormode(255)
leo.color(226, 0, 255)

leo.speed(1)

leo.penup()
leo.goto(0, 0)
leo.pendown()

side_length: float = 50
leo.begin_fill()
# code for shape being filled
i: int = 0 
while (i < 5): 
    leo.forward(side_length)
    leo.left(144)
    leo.forward(side_length)
    leo.left(72 - 144)
    i = i + 1 
leo.end_fill()

leo.hideturtle()


# bob: Turtle = Turtle()
# bob.color(0, 0, 0)

# bob.speed(10000)

# bob.penup()
# bob.goto(-150, -100)
# bob.pendown()

# i: int = 0 
# while (i < 150): 
#     side_length = side_length * 0.97
#     bob.forward(side_length)
#     bob.left(121)
#     i = i + 1 
# bob.hideturtle()

done()