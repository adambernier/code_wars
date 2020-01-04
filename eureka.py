def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    l = []
    for i in range(a,b+1):
        total = 0
        for idx,j in enumerate(map(int,list(str(i)))):
            total += j ** (idx+1)
        if total == i:
            l.append(i)
    return l
