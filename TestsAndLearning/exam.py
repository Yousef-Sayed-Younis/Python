# my_var = 8
# if my_var % 2:
#     if my_var ** 3 != 18:
#         my_var = my_var + 4
#     else:
#         my_var /= 1.5

# else:
#     if my_var <= 10:
#         my_var *= 2
#     else:
#         my_var -= 2

# print(my_var)


# def func():
#     num = 1.0
#     tot = 0
#     while num < 100:
#         tot = 1 // num
#         num += 1
#     return tot

# print(func())


s = "aaabccddd"

string = list(s)

for i in range(len(s) - 1):
    try:
        if string[i + 1] == string[i]:
            try:
                string.pop(i + 1)
                string.pop(i)
            except:
                pass
    except:
        pass
print("".join(string))
