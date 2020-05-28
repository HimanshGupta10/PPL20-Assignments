#importing a paritcular module for abstraction
import abc
from math import pi

#Abstract Class
class Shape(metaclass = abc.ABCMeta):
	#Abstract Methods
	# Virtual Methods
	@abc.abstractmethod
	def setSides(self):
		pass
	@abc.abstractmethod
	def getArea(self):
		pass
	@abc.abstractmethod
	def getPerimeter(self):
		pass
	@abc.abstractmethod
	def getSides(self):
		pass
	@abc.abstractmethod
	def getNumberSides(self):
		pass

#Abstraction
class Square(Shape):	
	def __init__(self, side = 0):
		super.__init__()
		#Private Variable
		self.__numberOfSides = 4	
		self.__side = max(side, 0)
	# Overriding
	def setSides(self, side = 0):
		self.__side = max(side, 0)
	def getArea(self):
		return self.__side * self.__side
	def getPerimeter(self):
	 return 4 * self.__side
	def getSides(self):
	 return self.__side
	def getNumberSides(self):
	 return self.__numberOfSides

class Rectange(Shape):	#Abstraction
	def __init__(self, length = 0, breadth = 0):
		super().__init__()
		self.__numberOfSides = 4	#Private Variable
		self.__length = max(length, 0)
		self.__breadth = max(breadth, 0)
	#Overriding abstract methods
	#Virtual functions
	def setSides(self, length = 0, breadth = 0):
		self.__length = max(length, 0)
		self.__breadth = max(breadth, 0)
	def getArea(self):
		return self.__length * self.__breadth
	def getPerimeter(self):
	 return 2 * (self.__length + self.__breadth)
	def getSides(self):
	 return [self.__length, self.__breadth]
	def getNumberSides(self):
	 return self.__numberOfSides



class Parallelogram(Shape):
	def __init__(self, side = 0, base = 0):
		super().__init__()
		self.__numberOfSides = 4	#Private Variable
		self.__side = max(side, 0)
		self.__base = max(base, 0)
	def setSides(self, side = 0, base = 0):
		self.__side = max(side, 0)
		self.__base = max(base, 0)
	def getArea(self):
		return max(int(input("Enter height of parallelogram ")), 0) * self.__base
	def getPerimeter(self):
	 return 2 * (self.__side + self.__base)
	def getSides(self):
	 return [self.__side, self.__base]
	def getNumberSides(self):
	 return self.__numberOfSides

# Encapsulation
class Ellipse:
	def __init__(self, minor = 0, major = 0):
		self.__minor = max(minor, 0)
		self.__major = max(major, 0)
	def setAxis(self, minor = 0, major = 0):
		self.__minor = max(minor, 0)
		self.__major = max(major, 0)
	def getArea(self):
		return pi * self.__minor * self.__major
	def getPerimeter(self):
		root = ((self.__minor ** 2) + (self.__major ** 2)) / 2
		value = root ** 0.5
		return 2 * pi * value
	def getAxis(self):
		return [self.__minor, self.__major]

class Rhombus(Shape):
	def __init__(self, side = 0):
		super.__init__()
		self.__numberOfSides = 4
		self.__side = max(side, 0)
	def setSides(self, side = 0):
		self.__side = max(side, 0)
	def getArea(self):
		return max(int(input("Enter altitude of rhombus ")), 0) * self.__side
	def getPerimeter(self):
	 return 4 * self.__side
	def getSides(self):
	 return self.__side
	def getNumberSides(self):
	 return self.__numberOfSides

class Pentagon:
	def __init__(self, side = 0):
		self.__numberOfSides = 5
		self.__side = max(side, 0)
	def setSides(self, side = 0):
		self.__side = max(side, 0)
	def getArea(self):
		value = (5 * (5 + 2 * (5 ** 0.5))) ** 0.5
		return (1 / 4) * value * (self.__side ** 2)
	def getPerimeter(self):
	 return 5 * self.__side
	def getSides(self):
	 return self.__side
	def getNumberSides(self):
	 return self.__numberOfSides

class Hexagon(Shape):
	def __init__(self, side = 0):
		self.__numberOfSides = 6
		self.__side = max(side, 0)
	def setSides(self, side = 0):
		self.__side = max(side, 0)
	def getArea(self):
		return (3 / 2) * (3 ** 0.5) * (self.__side ** 2)
	def getPerimeter(self):
	 return 6 * self.__side
	def getSides(self):
	 return self.__side
	def getNumberSides(self):
	 return self.__numberOfSides

class Triangle(Shape):
	def __init__(self, a = 0, b = 0, c = 0):
		self.__numberOfSides = 3
		self.__a, self.__b, self.__c = max(a, 0), max(b, 0), max(c, 0)
	def setSides(self, a = 0, b = 0, c = 0):
		self.__a, self.__b, self.__c = max(a, 0), max(b, 0), max(c, 0)
	def getArea(self):
		semi = (self.__a + self.__b + self.__c) / 2
		root = semi * (semi - self.__a) * (semi - self.__b) * (semi - self.__c)
		return root ** 0.5
	def getPerimeter(self):
		return sum([self.__a, self.__b, self.__c])
	def getSides(self):
		return [self.__a, self.__b, self.__c]
	def getNumberSides(self):
		return self.__numberOfSides


#Parent / Super Class
class Circle:	#Base Class
	def __init__(self, radius = 0):
		self.__radius = max(radius, 0)
	def setRadius(self, radius = 0):
		self.__radius = max(radius, 0)
	def getRadius(self):
		return self.__radius
	def getArea(self):
		return pi * self.__radius * self.__radius
	def getPerimeter(self):
		return 2 * pi * self.__radius

#Subclass / Parent = Circle
#Polymorphism with inheritance and some methods overriden
class Sphere(Circle):
	def __init__(self, radius=0):
	 super().__init__(radius=radius)
	#Method override
	def getArea(self):
	 return 4 * super().getArea()
	def getVolume(self):
		return (4/3) * pi * (self._Circle__radius ** 3)
