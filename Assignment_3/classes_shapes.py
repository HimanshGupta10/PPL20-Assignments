import math
import turtle

class rectangle():
    def __init__(self, side1, side2):
        self.a = side1
        self.b = side2
        cat = 'Polygon'
        self.scale = 10
    def getarea(self):
        self._area = (self.a*self.b)
        print("Area is ".format(self._area))
    def getperimeter(self):
        self._perimeter = 2*(self.a+self.b)
        print("Perimeter is ".format(self._perimeter))
    def getcategory(self):
        print('It is a '+ self.cat)
    def draw(self):
        turtle.clear()
        turtle.forward(self.a*self.scale)
        turtle.left(90)
        turtle.forward(self.b*self.scale)
        turtle.left(90)
        turtle.forward(self.a*self.scale)
        turtle.left(90)
        turtle.forward(self.b*self.scale)
        turtle.done()

class square():
    def __init__(self, side):
        self.a = side
        cat = 'Polygon'
        self.scale = 10
    def getarea(self):
        self._area = (self.a*self.a)
        print("Area is ".format(self._area))
    def getperimeter(self):
        self._perimeter = 2*(self.a+self.a)
        print("Perimeter is ".format(self._perimeter))
    def getcategory(self):
        print('It is a '+ self.cat)
    def draw(self):
        turtle.clear()
        turtle.forward(self.a*self.scale)
        turtle.left(90)
        turtle.forward(self.a*self.scale)
        turtle.left(90)
        turtle.forward(self.a*self.scale)
        turtle.left(90)
        turtle.forward(self.a*self.scale)
        turtle.done()
        


class scalenetriangle():
    def __init__(self, a,b,c,theta1,theta2):
        self.a = a
        self.b = b
        self.c = c
        self.theta1 = theta1
        self.theta2 = theta2
        self.cat = 'Polygon'
        self.scale = 10
    def getperimeter(self):
        self._perimeter = self.a + self.b + self.c
        print("Perimeter is".format(self._perimeter))
    def draw(self):
        turtle.clear()
        turtle.forward(self.a*self.scale)
        turtle.left(180 - self.theta1)
        turtle.forward(self.b*self.scale)
        turtle.left(180 - self.theta2)
        turtle.forward(self.c*self.scale)
        turtle.done()

class equilateraltriangle():
    def __init__(self, a):
        self.a = a
        self.b = a
        self.c = a
        self.theta1 = 60
        self.theta2 = 60
        self.cat = 'Polygon'
        self.scale = 10
    def getperimeter(self):
        self._perimeter = self.a + self.b + self.c
        print("Perimeter is".format(self._perimeter))
    def draw(self):
        turtle.clear()
        turtle.forward(self.a*self.scale)
        turtle.left(180 - self.theta1)
        turtle.forward(self.b*self.scale)
        turtle.left(180 - self.theta2)
        turtle.forward(self.c*self.scale)
        turtle.done()
        
class circle():
    def __init__(self, radius):
        self.radius = radius
        self.scale = 10
    def getperimeter(self):
        self._perimeter = (2*3.14*self._radius)
        print("Perimeter is {}".format(self._perimeter))
    def draw(self):
        turtle.clear()
        turtle.circle(self.radius*scale)
        turtle.done()

class rhombus():
    def __init__(self,a):
        self.a = a
        self.scale = 10
    def set_cat(self):
        self._cat = 'Polygon '   
        print(self.sides)
    def draw(self):
        
        turtle.forward(self.a * self.scale)
        turtle.left(60)
        turtle.forward(self.a * self.scale)
        turtle.left(120)
        turtle.forward(self.a * self.scale)
        turtle.left(60)
        turtle.forward(self.a * self.scale)
        turtle.done()
        
class pentagon():
    def __init__(self, a):
        self._a = a
        self.scale = 10
    def getperimeter(self):
        self._perimeter = (5*self._a)
        print("Perimeter is ".format(self._perimeter))
    def draw(self):
        turtle.clear()
        for i in range(5): 
            turtle.forward(self._a*self.scale) 
            turtle.right(72)
        turtle.done()
        
class hexagon():
    def __init__(self, a):
        self._a = a
        self.scale = 10
    def getperimeter(self):
        self._perimeter = (6*self._a)
        print("Perimeter is ".format(self._perimeter))
    def draw(self):
        turtle.clear()
        for i in range(6): 
            turtle.forward(self._a*self.scale) 
            turtle.right(60)
        turtle.done()
