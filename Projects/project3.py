#start
import turtle

t = turtle.Turtle()

t.goto(100, 0)
t.color("pink")
turtle.Screen() .bgcolor("black")

# first shape

for i in range(200):
    t.forward(100 + i)
    t.left(72 + 1)
t.speed(10)

#new shape
import turtle 

t = turtle.Turtle()

t.goto(50, -200)
t.color("cyan")

for i in range(200):
    t.forward(100 + i)
    t.left(60 + 1)
t.speed(10)

turtle.exitonclick()