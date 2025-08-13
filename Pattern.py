from turtle import *
from colorsys import hsv_to_rgb

tracer(50)
bgcolor("black")
pensize(3)

h = 0
for i in range(350):
    h += 0.0021
    c = hsv_to_rgb(h % 1, 1, 1)  # Cycle hue smoothly
    color(c)
    goto(0, 0)
    circle(180 - i/4, 90)
    circle(40)
    circle(180 - i/4, -60)
    right(50)

done()
