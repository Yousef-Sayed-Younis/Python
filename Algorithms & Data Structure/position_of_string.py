def p(string):
    if len(string) <= 2:
        return print(string[0])
    else:
        if len(string) % 2 == 0:
            return print(string[-2]), p(string[:-2])
        else:
            return print(string[-1]), p(string[:-2])