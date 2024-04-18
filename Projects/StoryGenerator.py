import random

names = ['Mohammed', 'Yousef', 'Gna', 'Zeyad', 'Salma', 'Karmin']
places = ['Cairo ', 'Dammam ', 'Gaza ', 'London ', 'Paris ']
quests = ['slaing the dragon', 'finding the treasure', 'eating the food', 'plaing video games']
roles = ['knight', 'witch', 'strong', 'player']

randomName = random.choice(names)
randomPlace = random.choice(places)
randomQuest = random.choice(quests)
randomRole = random.choice(roles)

story = 'Once upon a time there was a ' + randomRole + ' called ' + randomName + ' lives in ' + randomPlace + randomQuest + '.'

print(story)