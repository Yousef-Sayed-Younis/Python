A = [1, 2, 4, 5, 6, 6, 8, 9]
# A = [2, 5, 6, 7, 8, 8, 9]

def find_closest_num(A, target):
    min_diff = float("inf")
    low = 0
    high = len(A) - 1
    closest_num = None 

    # Edge Cases for empty lists or
    # When The List is only one Element
    if len(A) == 0:
        return None
    elif len(A) == 1:
        return A[0]

    while low <= high:
        mid = (low + high) // 2

        # Ensure we don't read beyond the bound of the list
        # And obtain the left and right difference values
        if mid + 1 < len(A):
            min_diff_right = abs(A[mid + 1] - target)

        if mid > 0:
            min_diff_left = abs(A[mid - 1] - target)

        # Check if the absolute value between left and right
        # Elements are smaller than any seen prior
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = A[mid - 1]

        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = A[mid + 1]

        # Move The Mid-Point Accordingly as is done
        # Via Binary Search
        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1

        # If The Element is The Target itself
        # The Closest number to it is itself
        else:
            return A[mid]
    
    return closest_num

y = find_closest_num(A, 11)
print(y)