import turtle
import random
import subprocess

CANVAS_SIZE = 500
DENSITY = 12

t = turtle.Turtle()
s = turtle.Screen()
s.setup(CANVAS_SIZE, CANVAS_SIZE)
s.bgcolor("blue")

def draw_line(row, col):
    lower_left = (
        (col * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2,
        (row * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2
    )
    upper_right = (
        ((col + 1) * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2,
        ((row + 1) * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2
    )

    t.goto(lower_left)
    t.pendown()
    t.color(random.random(), random.random(), random.random())
    t.goto(upper_right)
    t.penup()

def draw_random_lines():
    for row in range(DENSITY):
        for col in range(DENSITY):
            draw_line(row, col)

draw_random_lines()

# Save as EPS file
turtle_graphics_eps = "turtle_graphics.eps"
canvas = s.getcanvas()
canvas.postscript(file=turtle_graphics_eps)

# Convert EPS to PNG using Ghostscript
turtle_graphics_png = "turtle_graphics.png"
subprocess.run(['gswin64c', '-sDEVICE=png16m', '-r300', '-o', turtle_graphics_png, turtle_graphics_eps])

turtle.done()
