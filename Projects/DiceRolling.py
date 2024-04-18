import random

while True:
    print(random.randint(1, 6))
    again = input('Want to do it again? (y / n)\n').lower()
    if again == 'y':
        continue
    else:
        break