import turtle
bob = turtle.Turtle()
turtle.colormode(255)

#piece of the design
'''
def art1(sides,dist):
  for times in range(1000):
    bob.right(200)
    bob.circle(times * 5)
    bob.forward(100)
    bob.right(10)
    bob.right(30)
    angle=360/sides
    bob.color("orange")
    bob.begin_fill()
    bob.forward(10)
    bob.end_fill()

def art2(sides,dist):
  for times in range(50):
    bob.right(5)
    bob.circle(times * 10)
    bob.forward(10)
    bob.right(4)
    bob.right(3)
    angle=360/sides
    bob.color("pink")
    bob.begin_fill()
    bob.forward(2)
    bob.end_fill()


def art3(sides,dist):
  for times in range(100):
    bob.right(10)
    bob.circle(times * 7)
    bob.forward(10)
    bob.right(40)
    bob.right(30)
    angle=360/sides
    bob.color("black")
    bob.begin_fill()
    bob.forward(32)
    bob.end_fill()
'''

#definitons

def circle(radius, border_color, fill_color):
  bob.pencolor(border_color)
  bob.fillcolor(fill_color)
  bob.begin_fill()
  bob.circle(radius)
  bob.end_fill()
  
def polygon(sides, dist, color):
  angle = 360/sides
  bob.fillcolor(color)
  bob.begin_fill()
  for times in range(sides):        
    bob.forward(dist)
    bob.left(angle)
  bob.end_fill()

def jump(x,y):
  bob.penup()   
  bob.goto(x,y)
  bob.pendown()
  
#main design using repeating circles to make design
  
def art2(sides,dist):
  for times in range(2000):
    bob.right(10)
    bob.circle(times * 10)
    bob.forward(10)
    bob.right(40)
    bob.right(30)
    polygon(30,7,(106,13,173))
    angle=360/sides
    bob.pencolor((0,0,0))
    bob.color((255,0,255))
    bob.begin_fill()
    bob.forward(32)
    bob.end_fill()
'''

def art3(sides,dist):
  for times in range(100):
    bob.right(10)
    bob.circle(times * 7)
    bob.forward(10)
    bob.right(40)
    bob.right(30)
    angle=360/sides
    bob.color("black")
    bob.begin_fill()
    bob.forward(32)
    bob.end_fill()

'''
