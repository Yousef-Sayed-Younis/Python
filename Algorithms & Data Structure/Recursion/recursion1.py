string = "HelloWorld"

# By Me :)
# def iterative_str_len(string):
#     count = 0
#     clone_str = ''
#     while clone_str != string:
#         clone_str += string[count]
#         count += 1

#     return count

def iterative_str_len(string):
    count = 0
    for i in range(len(string)):
        count += 1
    return count

def recursive_str_len(string):
    if string == '':
        return 0
    
    return 1 + recursive_str_len(string[1:])


print(recursive_str_len(string))
print(iterative_str_len(string))