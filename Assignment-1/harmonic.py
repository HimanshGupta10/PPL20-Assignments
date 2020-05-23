print('first ten harmonic numbers')
i = 1
p = 0
fac = 0
add = 0
while p != 10:
    fac = 0
    add = 0
    if(i == 1):
        print(i)
        p += 1
        i += 1
        continue 
    for x in range(1, i//2 + 1):
        if i % x == 0:
            fac += 1
            add += i / x
    fac += 1
    add += 1
    if((fac * i) / add) == int((fac * i) / add):
        print(i)
        p += 1        
    i += 1