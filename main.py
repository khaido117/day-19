from turtle import Turtle, Screen
import random 

is_race_on = False 
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make Your Bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "pink", "green", "orange", "blue"]
y_positions = [-100, -60, -20, 20, 60]

for turtle_index in range(0, 5):  # Changed the range to 5 to match the length of colors and y_positions
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-240, y=y_positions[turtle_index])

    
# Removed screen.exitonclick()
screen.exitonclick()

