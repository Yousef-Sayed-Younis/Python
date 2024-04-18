def Fibonacci(n, x = 0, y = 0, i = 0):
    if i == 7:
        return 0
    
    print(n, end="\t")
    if y == 0:
    	y = n
    
    s = x + y
    
    return Fibonacci(s, y, s, i + 1)

Fibonacci(2)