class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def display(self):
        return f"Name is {self.name} and age is {self.age}"

# Inheritance
class Man(Person):
    gender = 'Male'
    NO_men = 0

    def __init__(self, name, age, voice = None):
        # To Inherit
        super().__init__(name, age)

        self.voice = voice
        Man.NO_men += 1


    # Dander Method
    def __lt__(self, other):
        return self.age < other.age

    def __add__(self, other):
        names = self.name + " and " + other.name
        ages = self.age + other.age
        return f"Names combined are {names} and sum of ages is {ages}"


    # Polymorphism
    def display(self):
        # Over Writing
        string = super().display()
        return f'{string} and voice is {self.voice} and gender is {self.gender}'


man = Man("Yousef", 20, 'Thick')
man1 = Man("Ahmed", 30)

print(man.display())
print(Man.NO_men)

print(man < man1)
print(man + man1)

print(dir(Man))