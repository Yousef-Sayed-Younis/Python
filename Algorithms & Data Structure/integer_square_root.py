import math

# Example:
    # Input is integer 300
    # output is 17, since 17^2 = 289 < 300. Note that 18^2 = 324 > 300.
    # So 17 is the correct responce.

k = 12

# By Me :)
# Time Complexity: O(1)
# Space Complexity: O(1)
def integer_square_root(k):
    for i in range(k - 1, 0, -1):
        if (pow(i, 0.5)).is_integer():
            return (int(pow(i, 0.5)))
    return None


def integer_square_root_1(k):
    low = 0
    high = k

    while low <= high:
        mid = (low + high) // 2
        mid_sqr = mid * mid

        if mid_sqr <= k:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1

print(integer_square_root_1(k))

print(integer_square_root(k))