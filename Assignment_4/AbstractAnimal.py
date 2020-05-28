#importing a paritcular module for abstraction
import abc

class Animal(metaclass = abc.ABCMeta):	#Abstract Class
    #Abstract Methods
    @abc.abstractclassmethod
    def setLegs(self):
        pass
    @abc.abstractclassmethod
    def setEyes(self):
        pass
    @abc.abstractclassmethod
    def setEars(self):
        pass
    @abc.abstractclassmethod
    def setColor(self):
        pass
    @abc.abstractclassmethod
    def setSpeak(self):
        pass
    @abc.abstractclassmethod
    def getLegs(self):
        pass
    @abc.abstractclassmethod
    def getEyes(self):
        pass
    @abc.abstractclassmethod
    def getEars(self):
        pass
    @abc.abstractclassmethod
    def getColor(self):
        pass
    @abc.abstractclassmethod
    def getSpeak(self):
        pass

class Dog(Animal):      #Abstraction
    def __init__(self, sound = None):
        super().__init__()
        self.__legs = 4 #Private Variable
        self._eyes = 2
        self.ears = 2   #Public Variable
        self.color = "Brown"
        self.__speak = sound
    #Overriding abstract methods
	#Virtual functions
    def setLegs(self, noOfLegs):
        self.__legs = noOfLegs
    def setEyes(self, noOfEyes):
        self._eyes = noOfEyes
    def setEars(self, noOfEars):
        self.ears = noOfEars
    def setColor(self, color):
        self.color = color
    def setSpeak(self, sound):
        self.__speak = sound
    def getLegs(self):
        return self.__legs
    def getEyes(self):
        return self._eyes
    def getEars(self):
        return self.ears
    def getColor(self):
        return self.color
    def getSpeak(self):
        return self.__speak

class Cat(Animal):      #Abstraction
    def __init__(self, sound = None):
        super().__init__()
        self.__legs = 4 #Private Variable
        self._eyes = 2
        self.ears = 2   #Public Variable
        self.color = "White"
        self.__speak = sound
    #Overriding abstract methods
	#Virtual Functions
    def setLegs(self, noOfLegs):
        self.__legs = noOfLegs
    def setEyes(self, noOfEyes):
        self._eyes = noOfEyes
    def setEars(self, noOfEars):
        self.ears = noOfEars
    def setColor(self, color):
        self.color = color
    def setSpeak(self, sound):
        self.__speak = sound
    def getLegs(self):
        return self.__legs
    def getEyes(self):
        return self._eyes
    def getEars(self):
        return self.ears
    def getColor(self):
        return self.color
    def getSpeak(self):
        return self.__speak

#Parent / Super Class
class Donkey:	#Base Class
	def __init__(self, sound = None):
		self.__legs = 4
		self._eyes = 2
		self.ears = 2
		self.color = "Black"
		self.__speak = sound
	def setLegs(self, noOfLegs):
		self.__legs = noOfLegs
	def setEyes(self, noOfEyes):
		self._eyes = noOfEyes
	def setEars(self, noOfEars):
		self.ears = noOfEars
	def setColor(self, color):
		self.color = color
	def setSpeak(self, sound):
		self.__speak = sound
	def getLegs(self):
		return self.__legs
	def getEyes(self):
		return self._eyes
	def getEars(self):
		return self.ears
	def getColor(self):
		return self.color
	def getSpeak(self):
		return self.__speak

	def isGoat(self):
		return False
	def isSheep(self):
		return False
	def hasFurr(self):
		return False

#Subclass / Parent = Donkey
#Polymorphism with inheritance and some methods overriden
class Sheep(Donkey):	#Derived Class
	def __init__(self, sound=None):
	 super().__init__(sound=sound)
	#Method Override
	def hasFurr(self):
	 return not super().hasFurr()
	def isSheep(self):
	 return not super().isSheep()
	def isGoat(self):
	 return super().isGoat()

#Subclass / Parent = Donkey
#Polymorphism with inheritance and some methods overriden
class Goat(Donkey):	#Derived Class
	def __init__(self, sound=None):
	 super().__init__(sound=sound)
	#Method Override
	def hasFurr(self):
	 return super().hasFurr()
	def isSheep(self):
	 return super().isSheep()
	def isGoat(self):
	 return not super().isGoat()

class Lion:
	def __init__(self, sound = None):
		super().__init__()
		self.__legs = 4
		self._eyes = 2
		self.ears = 2
		self.color = "Crimson" 
		self.__speak = sound
	def setLegs(self, noOfLegs):
		self.__legs = noOfLegs
	def setEyes(self, noOfEyes):
		self._eyes = noOfEyes
	def setSpeak(self, sound):
		self.__speak = sound
	def setColor(self, color):
		self.color = color
	def setEars(self, noOfEars):
		self.ears = noOfEars
	def getLegs(self):
		return self.__legs
	def getEyes(self):
		return self._eyes
	def getSpeak(self):
		return self.__speak
	def getColor(self):
		return self.color
	def getEars(self):
		return self.ears

	def hasTail(self):
		return True

class Tiger:
	def __init__(self, sound = None):
		super().__init__()
		self.__legs = 4
		self._eyes = 2
		self.ears = 2
		self.color = "Brown-Striped" 
		self.__speak = sound
	def setLegs(self, noOfLegs):
		self.__legs = noOfLegs
	def setEyes(self, noOfEyes):
		self._eyes = noOfEyes
	def setSpeak(self, sound):
		self.__speak = sound
	def setColor(self, color):
		self.color = color
	def setEars(self, noOfEars):
		self.ears = noOfEars
	def getLegs(self):
		return self.__legs
	def getEyes(self):
		return self._eyes
	def getSpeak(self):
		return self.__speak
	def getColor(self):
		return self.color
	def getEars(self):
		return self.ears

	def hasTail(self):
		return True

class Rabbit:
	def __init__(self, sound = None):
		super().__init__()
		self.__legs = 4
		self._eyes = 2
		self.ears = 2
		self.color = "White" 
		self.__speak = sound
	def setLegs(self, noOfLegs):
		self.__legs = noOfLegs
	def setEyes(self, noOfEyes):
		self._eyes = noOfEyes
	def setSpeak(self, sound):
		self.__speak = sound
	def setColor(self, color):
		self.color = color
	def setEars(self, noOfEars):
		self.ears = noOfEars
	def getLegs(self):
		return self.__legs
	def getEyes(self):
		return self._eyes
	def getSpeak(self):
		return self.__speak
	def getColor(self):
		return self.color
	def getEars(self):
		return self.ears

	def hasTail(self):
		return True

class Elephant:
	def __init__(self, sound = None):
		super().__init__()
		self.__legs = 4
		self._eyes = 2
		self.ears = 2
		self.color = "Grey" 
		self.__speak = sound
	def setLegs(self, noOfLegs):
		self.__legs = noOfLegs
	def setEyes(self, noOfEyes):
		self._eyes = noOfEyes
	def setSpeak(self, sound):
		self.__speak = sound
	def setColor(self, color):
		self.color = color
	def setEars(self, noOfEars):
		self.ears = noOfEars
	def getLegs(self):
		return self.__legs
	def getEyes(self):
		return self._eyes
	def getSpeak(self):
		return self.__speak
	def getColor(self):
		return self.color
	def getEars(self):
		return self.ears

	def hasTail(self):
		return True
	def hasTrunk(self):
		return True

class Bear:
	def __init__(self, sound = None):
		super().__init__()
		self.__legs = 4
		self._eyes = 2
		self.ears = 2
		self.color = "Brown" 
		self.__speak = sound
	def setLegs(self, noOfLegs):
		self.__legs = noOfLegs
	def setEyes(self, noOfEyes):
		self._eyes = noOfEyes
	def setSpeak(self, sound):
		self.__speak = sound
	def setColor(self, color):
		self.color = color
	def setEars(self, noOfEars):
		self.ears = noOfEars
	def getLegs(self):
		return self.__legs
	def getEyes(self):
		return self._eyes
	def getSpeak(self):
		return self.__speak
	def getColor(self):
		return self.color
	def getEars(self):
		return self.ears

	def hasTail(self):
		return True
