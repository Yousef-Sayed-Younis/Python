str1 = 'abc de'
str2 = 'HellOWrold'

vowels = ['a', 'e', 'o', 'i', 'u']
vowels = 'aeoiu'

def iterative_count_consonants(string):
    count = 0
    for i in range(len(string)):
        if string[i].lower() not in vowels and string[i].isalpha():
            count += 1
    return count


def recursion_count_consonants(string):
    if string == '':
        return 0

    elif string[0].lower() not in vowels and string[0].isalpha():
        return 1 + recursion_count_consonants(string[1:])
    
    else:
        return recursion_count_consonants(string[1:])
    

print(iterative_count_consonants(str1))
print(iterative_count_consonants(str2))

print(recursion_count_consonants(str1))
print(recursion_count_consonants(str2))