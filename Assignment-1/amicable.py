print('First ten amicable numbers')
a = 0
b = 0
p = 0
i = 1
add = 0
done = []
while p != 10:
    add = 0
    a = i
    for x in range(1, i//2 + 1):
        if i % x == 0:
            add += x
    if(add == a):
        i += 1
        continue
    b = add
    add = 0
    for x in range(1, b//2 + 1):
        if b % x == 0:
            add += x
    if add == a:
        if((a in done) and (b in done)):
            i += 1
            continue
        tup = (a,b)
        done.append(a)
        done.append(b)
        print(tup)
        p += 1
    i += 1