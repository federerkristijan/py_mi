import turtle
import random

# https://docs.python.org/3/library/turtle.html

radius = 100

CANVAS_SIZE = 500
DENSITY = 12

t = turtle.Turtle()
s = turtle.Screen()
s.setup(CANVAS_SIZE, CANVAS_SIZE)
s.bgcolor("blue")
# t.circle(radius)

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
   # t.color(R,G,B)
   t.color(random.random(), random.random(), random.random())
   t.goto(upper_right)
   t.penup()

def draw_random_lines():
   for row in range(DENSITY):
      for col in range(DENSITY):
         draw_line(row, col)

def draw_random_circles():

      for row in range(DENSITY):
         for col in range(DENSITY):
            lower_left = (
            (col * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2,
            (row * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2
            )
            upper_right = (
               ((col + 1) * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2,
               ((row + 1) * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2
            )
            radius = random.randint(10,50)
            t.penup()
            t.goto(upper_right)
            t.pendown()
            t.circle(radius)

# draw_line(10,30)
draw_random_lines()
draw_random_circles()

turtle.done()
