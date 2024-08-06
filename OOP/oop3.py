from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side 

    def area(self):
        return self.__side ** 2

    def perimeter(self):
        return self.__side * 4

class Rectangle(Shape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return (self.__length + self.__width) * 2


square = Square(10)
print(f"Square's area is {square.area()} and perimeter is {square.perimeter()}")
rect = Rectangle(5, 3)
print(f"Rectangle's area is {rect.area()} and perimeter is {rect.perimeter()}") 
