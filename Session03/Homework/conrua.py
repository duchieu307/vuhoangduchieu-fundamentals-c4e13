
color_turtle = ['red', 'blue', 'orange', 'yellow','grey']
from turtle import *
speed(1)
for i in range(3,8):

    for j in range(0,i):
        color(color_turtle[i-3])
        forward(100)
        left(360/i)


mainloop()
