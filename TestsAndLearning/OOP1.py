# Static Method

class Math:
    
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def multi(x, y):
        return x * y 

    @staticmethod
    def dive(x, y):
        return x / y 

    @staticmethod
    def subs(x, y):
        return x - y

addition = Math.add(5, 10)
multiplication = Math.multi(5, 10)
diversion = Math.dive(10, 5)
substract = Math.subs(10, 5)

print(addition, multiplication, diversion, substract)