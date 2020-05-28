class Animal():
    
    def __init__(self):
        self.name = '' 
        self.legs = 4
        self._color = ''
        self.__family  = '' 
    def getname(self):
        print("This is a", self.name)
    def getcolor(self):
        print(self._color)
    def getlegs(self):
        return self.legs
    def setlegs(self,legs):
        self.legs = legs
    def setname(self, name):
        self.name = name
    def setcolor(self, color):
        self._color = color
    def setfamily(self, family):
        self.__family = family
        
class Cat(Animal):
    def __init__(self):
        self.name = 'Cat' 
        self.legs = 4
        self._color = 'White'
        self.family = 'Mammal'
        self.fur = True
    def spill(self):        
        print('The '+self.name + ' has ' + str(self.legs) + ' legs and is ' + self._color + ' in color. It belongs to the ' + self.family + " Family.")
        


class Dog(Animal):
    def __init__(self):
        self.name = 'Dog' 
        self.legs = 4
        self._color = 'Brown / Black'
        self.family = 'Mammal'
        self.fur = True
    def spill(self):
        
        print('The '+self.name + ' has ' + str(self.legs) + ' legs and is ' + self._color + ' in color. It belongs to the ' + self.family + " Family.")

class Elephant(Animal):
    def __init__(self):
        self.name = 'Elephant' 
        self.legs = 4
        self._color = 'Gray'
        self.family = 'Mammal'
        self.fur = False
        self.size = "Large"
    def spill(self):
        print('The '+self.name + ' has ' + str(self.legs) + ' legs and is ' + self._color + ' in color. It belongs to the ' + self.family + " Family.")
        
class Wolf(Animal):
    def __init__(self):
        self.name = 'Wolf' 
        self.legs = 4
        self._color = 'Black'
        self.family = 'Mammal'
        self.fur = True
    def spill(self):
        
        print('The '+self.name + ' has ' + str(self.legs) + ' legs and is ' + self._color + ' in color. It belongs to the ' + self.family + " Family.")
        

class Fox(Animal):
    def __init__(self):
        self.name = 'Fox' 
        self.legs = 4
        self._color = 'Brown'
        self.family = 'Mammal'
        self.isDomestic = False
    def spill(self):
        
        print('The '+self.name + ' has ' + str(self.legs) + ' legs and is ' + self._color + ' in color. It belongs to the ' + self.family + " Family.")

class Lion(Animal):
    def __init__(self):
        self.name = 'Lion' 
        self.legs = 4
        self._color = 'Yellow'
        self.family = 'Mammal'
        self.fur = True
        self.isDomestic = False
    def spill(self):
        
        print('The '+self.name + ' has ' + str(self.legs) + ' legs and is ' + self._color + ' in color. It belongs to the ' + self.family + " Family.")
        


class Tiger(Animal):
    def __init__(self):
        self.name = 'Tiger' 
        self.legs = 4
        self._color = 'Orange'
        self.family = 'Mammal'
        self.fur = True
        self.isDomestic = False
    def spill(self):
        
        print('The '+self.name + ' has ' + str(self.legs) + ' legs and is ' + self._color + ' in color. It belongs to the ' + self.family + " Family.")



class Human(Animal):
    def __init__(self):
        self.name = 'Human' 
        self.legs = 2
        self._color = 'Yellow'
        self.family = 'Mammal'
        self.fur = False
    def spill(self):
        
        print('The '+self.name + ' has ' + str(self.legs) + ' legs and is ' + self._color + ' in color. It belongs to the ' + self.family + " Family.")

class Lizard(Animal):
    def __init__(self):
        self.name = 'Lizard' 
        self.legs = 2
        self._color = 'Yellow'
        self.family = 'Reptile'
        self.fur = False
        
    def spill(self):
        
        print('The '+self.name + ' has ' + str(self.legs) + ' legs and is ' + self._color + ' in color. It belongs to the ' + self.family + " Family.")
        

