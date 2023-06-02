import turtle
import random
from PIL import ImageGrab

radius = 100

CANVAS_SIZE = 500
DENSITY = 12

t = turtle.Turtle()
s = turtle.Screen()
s.setup(CANVAS_SIZE, CANVAS_SIZE)
s.bgcolor("green")
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

   # Farbe ändern
   # t.color(R,G,B)
   t.color(random.random(), random.random(), random.random())

   # # Linien, Stiftgröße ändern
   # line_length = random.randint(50, 150)
   # t.pensize(random.randint(1, 5))
   # t.forward(line_length)

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
# draw_random_circles()

# # als Image speichern
# canvas = s.getcanvas()
# canvas.postscript(file = "line_circle_graphics.eps")
# image = Image.open("line_circle_graphics.eps")
# image.save("turtle_image.png", "PNG")

# Screenshot machen -> Als Image speichern
image = ImageGrab.grab(bbox = (0, 0, CANVAS_SIZE, CANVAS_SIZE))
image.save("turtle_image.png", "PNG")

turtle.done()
