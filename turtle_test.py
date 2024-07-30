from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(height=750, width=800)
user_guess = screen.textinput(title="Make your guess.", prompt="Which color turtle you think is going to win?")

turtle_colors = ["red", "blue", "green", "yellow", "orange", "dark blue", "dark green"]
positions = [-300, -200, -100, 0, 100, 200, 300 ]
turtles = []

for i in range(0,7):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.penup()
    

    turtle.color(turtle_colors[i])
    turtle.goto(x=-385, y=positions[i])

    turtles.append(turtle)

game = True

while game:

    for turtle in turtles:
        if turtle.xcor() > 380:
            game = False

        distance = random.randint(5, 15)
        turtle.forward(distance)















screen.exitonclick()



