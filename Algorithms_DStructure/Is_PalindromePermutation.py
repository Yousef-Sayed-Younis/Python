# Palindrome = "racecar"
# Permuted Plaindrome = "acecarr"

# Taco Cat
palin_perm = "Tact Coa" 
not_palin_perm = "This is not a Palindrome Permutation"

# Time Complexity O(n)
# Space Comlexity O(n)
def is_palin_perm(int_str):
    int_str = int_str.replace(" ", "")
    int_str = int_str.lower()
    
    d = dict()

    for i in int_str:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    odd_count = 0
    for k, v in d.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False

    return True

print(is_palin_perm(palin_perm))
print(is_palin_perm(not_palin_perm))