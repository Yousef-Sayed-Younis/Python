NAMES = []
NUMBERS = []

def addNumber():
    name = input('Name: ')
    number = input('Phone: ')
    NAMES.append(name)
    NUMBERS.append(number)

def show():
    if len(NAMES) == 0:
        print('There is NO Contact.')
    else:
        for i in range(len(NAMES)):
            print(i, NAMES[i], NUMBERS[i])
        print('\n')

while True:
    answer = input("1)  Add number.\n2)  Show numbers.\n3)  Delete number.\n4)  Edit number.\n5)  End.\n")
    if answer == '1':
        addNumber()
    elif answer == '2':
        show()
    elif answer == '3':
        show()
        delete = int(input('Choose id for delete: '))
        NAMES.pop(delete)
        NUMBERS.pop(delete)
    elif answer == '4':
        show()
        edit = int(input("Choose id for edit: "))
        name = input('Enter New Name: ')
        number = input('Enter New Number: ')
        NAMES[edit] = name
        NUMBERS[edit] = number
    elif answer == '5':
        break
    else:
        print('Invalid input, Try Again.')