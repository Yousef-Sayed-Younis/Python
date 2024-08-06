from datetime import date

class Student: # Capital Letter For Any Name Of Class
    # Class Attribute
    NO_students = 0
    # Can Make Only One __init__ In The Class
    def __init__(self, name, age = None, courses = None): # Self Is Must Be In The First
        # Instance Attribute / Private Attribute
        self.name = name
        self.age = age
        self.courses = courses
        Student.NO_students += 1

    # Encapsulation
    # Getters & Sitters
    def get_name(self):
        return self.name

    def change_name(self, new_name):
        self.name = new_name

    # Instance Methods
    # Should Have self To Access Information
    def describe(self):
        print(f'My name is {self.name} and my age is {self.age}.')

    def is_old(self, num):
        if self.age <= num:
            print("Student isn't old")
        else:
            print("Student is old")

    # Class Method
    # Can Make Many Of classmethod
    @classmethod
    def initFromBirthYear(cls, name, birthYear): # cls Must Be In The First
        return cls(name, date.today().year - birthYear)

class Pizza:
    def __init__(self, radius, ingredients = None):
        self.ingredients = ingredients
        self.radius = radius

    @classmethod
    def veg(cls):
        return cls(['Mushrooms', 'Olives', 'Onions'])

    @classmethod
    def margherita(cls):
        return cls(['Mozzarella', 'Sauce'])

    def area(self):
        return Pizza.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * 3.14

    # Return Value In String Not In ID
    def __str__(self):
        return f'Pizza ingredients are {self.ingredients}'


pizza1 = Pizza(['Tomatoes', 'Olives'])
pizza2 = Pizza.veg()
pizza3 = Pizza.margherita()

print(pizza2, pizza3)

pizza = Pizza(5)

print(pizza.area())
print(Pizza.circle_area(6))
print(Pizza.circle_area(10))
