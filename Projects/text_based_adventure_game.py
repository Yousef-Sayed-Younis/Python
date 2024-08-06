
answer = input("Would you like to play? (yes / no)\n")

if answer.lower().strip() == 'yes':
    answer = input("You reach a crossroads, You will go left or right?\n").lower().strip()
    if answer == 'left':
        answer = input("You are under attack, You Fight or Run?\n").lower().strip()
        if answer == 'fight':
            print('A prave fighter!!')
        elif answer == 'Run':
            print('A coward')
        else:
            print('Try Again')
    elif answer == 'right':
        answer = input("You find a girl need help, You (help or leave) her?\n").lower().strip()
        if answer == 'help':
            print('You are a Hero!')
        elif answer == 'leave':
            print('You are a B!tch')
        else:
            print('Try Again')
    else:
        print('You Lost!')
else:
    print("It's Okay :)")