x = 5
y = 3

def iternative_product(x, y):
    result = 0
    for i in range(x):
        result += y

    return result


def recursive_product(x, y):

    # To Prevent Exceeding Maximum Recursion Depth
    if x < y:
        return recursive_product(y, x)

    if y == 0:
        return 0
    else:
        return x + recursion_product(x, y-1)

print(iternative_product(x, y))
print(recursion_product(x, y))