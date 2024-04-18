def number(a):
    return a[a.find('0'):]
a = ("b0.9", "g0.6", "a0.8", "d0.5", "f0.7", "c0.4", "h0.3", "e0.2")
x = sorted(a, key=number, reverse=True)
print(x)