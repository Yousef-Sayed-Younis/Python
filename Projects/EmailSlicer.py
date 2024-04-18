email = input('Enter Your Email: ')

userName = email[:email.index('@')]

domain = email[email.index('@') + 1:]

print(f'Your username is: {userName}, and your domain is: {domain}')