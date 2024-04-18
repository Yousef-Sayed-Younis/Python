# Fixed Point is an index i is equal to i

# Fixed Point is 3
#     0    1  2  i = 3
A = [-10, -5, 0, 3, 7]

# Fixed Point is 0
#    i = 0
A = [0, 2, 5, 8, 17]

# No Fixed Point. Return 'None'
A = [-10, -5, 3, 4, 7, 9]

# Time Complexity: O(n)
# Space Complexity: O(1)
def find_fixed_point_linear(A):
    for i in range(len(A)):
        if A[i] == i:
            return A[i]
    return None

# Time Complexity: O(log n)
# Space Complexity: O(1)
def find_fixed_point(A):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 

        if A[mid] < mid:
            low = mid + 1
        elif A[mid] > mid:
            high = mid - 1
        else:
            return A[mid]

    return None

print(find_fixed_point(A))