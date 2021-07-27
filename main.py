from turtle import Turtle, Screen

t = Turtle()
s = Screen()

s.colormode(255)
s.bgcolor(110, 162, 245)
t.color(119, 61, 166)

string = 'Mr. Ravenberry'
t.shapesize(2,2,1)
t.backward(160)
t.write(string, font = ("Arial", 15, 'normal'))
