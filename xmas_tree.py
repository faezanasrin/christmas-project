from turtle import *

speed(0)

# Background
penup()
goto(0,-250)
pendown()
color("maroon")
begin_fill()
circle(270)
end_fill()

# Tree Trunk
penup()
goto(-15,-50)
pendown()
color("brown")
begin_fill()
for i in range(2):
    forward(30)
    right(90)
    forward(40)
    right(90)
end_fill()

# Set the start position and the initial tree width
y = -50
width = 240
height = 25

# Green section of the tree
while width > 20:
    width = width - 30 # Make the tree get smaller as it goes up in the height
    x = 0 - width / 2 # Set the starting x-value of each level of the tree
    color("green")
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

    y = y + height # keep drawing the levels of the tree higher than the previous

# star
penup()
goto(-15, 150)
pendown()
color("gold")
begin_fill()
for i in range(5):
    forward(30)
    right(144)
end_fill()

#decoration
penup()
goto(20, 40)
pendown()
color("red")
begin_fill()
for i in range(5):
    forward(20)
    right(144)
end_fill()

penup()
goto(-30, 80)
pendown()
color("lightblue")
begin_fill()
for i in range(5):
    forward(20)
    right(144)
end_fill()

penup()
goto(-40,-30)
pendown()
color("pink")
begin_fill()
for i in range(5):
    forward(20)
    right(144)
end_fill()

penup()
goto(30,-30)
pendown()
color("darkorange")
begin_fill()
for i in range(5):
    forward(20)
    right(144)
end_fill()

penup()
goto(-20,20)
pendown()
color("pink")
begin_fill()
circle(10)
end_fill()

penup()
goto(-60,-20)
pendown()
color("firebrick")
begin_fill()
circle(10)
end_fill()

penup()
goto(30,-20)
pendown()
color("lightblue")
begin_fill()
circle(10)
end_fill()

#writings
penup()
goto(-210,-150)
color("white")
write("MERRY CHRISTMAS AND HAPPY NEW YEAR!",font=("Arial",15,"bold"))
penup()
goto(85,-170)
color("white")
write("-faeza nasrin",font=("Arial",15,"bold"))

hideturtle()











