#polymorphism [Many n Forms] = means having many faces nd forms 
#ways :- inheritance , duck typing 
from abc import ABC, abstractmethod
class Shape:
    
    @abstractmethod          #decorater
    def area(self):
        pass
    pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

   
class Square(Shape):

    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side ** 2 

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

class Pizza(Circle):
    def __init__(self,toppings):
        self.toppings = toppings
        super().__init__(radius=2)


shapes = [Circle(2), Square(2), Triangle(3,4), Pizza("pepporani")]

for shape in shapes:
    print(shape.area())

#need another tutorials 