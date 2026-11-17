from myfunctions import *


from random import*

turtle.bgcolor("black")
turtle.tracer(0)
turtle.colormode(255)
bob.width(1)
art2(11,100)


#code for repeating white circles in random areas.

num = randint(100, 200)

for times in range( num ):
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  border = (0,0,0)
  fill = (255,255,255)
  x = randint(-1000,1000)
  y = randint(-1000,1000)
  radius = randint(5,10)
  circle(radius, border, fill )
  jump(x,y)
