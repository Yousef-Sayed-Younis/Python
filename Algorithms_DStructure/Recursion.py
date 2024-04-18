str1 = 'helloWorld'
str2 = 'HelloWorld'
str3 = 'helloworld'

def Find_uppercase_iterative(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return input_str[i]

    return "NO uppercase character found"


def find_uppercase_recursive(input_str, index = 0):
    if index == len(input_str) - 1:
        return "NO uppercase character found"

    elif input_str[index].isupper():
        return input_str[index]
        
    return find_uppercase_recursive(input_str, index + 1)


print(Find_uppercase_iterative(str1))
print(Find_uppercase_iterative(str2))
print(Find_uppercase_iterative(str3))

print(find_uppercase_recursive(str1))
print(find_uppercase_recursive(str2))
print(find_uppercase_recursive(str3))