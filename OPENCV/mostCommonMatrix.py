Matrix = [  ['G', 'A', 'C', 'E', 'C', 'F'],
            ['B', 'C', 'F', 'A', 'A', 'F'],
            ['F', 'A', 'G', 'B', 'A', 'D'],
            ['F', 'F', 'G', 'A', 'C', 'C'],
            ['E', 'E', 'F', 'A', 'E', 'D'],
            ['C', 'E', 'F', 'B', 'G', 'A'],
            ['D', 'A', 'D', 'C', 'F', 'D'], 
            ['D', 'F', 'A', 'G', 'D', 'C']
        ]

chars = {}
def mostMatrix(Matrix, j = 0):
    row = len(Matrix)
    column = len(Matrix[0])

    for i in range(row):
        char = Matrix[i][j]

        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    
    if j == column - 1:

        listOfMax = []
        maximum = max(chars, key=chars.get)

        for key, value in chars.items():
            if value == chars[maximum]:
                listOfMax.append(key)
        
        if len(listOfMax) == 1:
            return print('The most common characters are:', listOfMax[0])
        elif len(listOfMax) == 2:
            return print('The most common characters are:', listOfMax[0] + ' and ' + listOfMax[1])
        elif len(listOfMax) > 2:
            return print('The most common characters are:', listOfMax)
        else:
            return print('Matrix is Empty')
    else:
        j += 1
        return mostMatrix(Matrix, j)

mostMatrix(Matrix)