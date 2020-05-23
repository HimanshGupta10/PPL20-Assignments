print('Finding missing pages')
print('Enter list of pages present one by one press \'q\' to stop Entering')
i = 1
pge = []
while True:
    a = input()
    if(a != 'q'):
        pge.append(a)
    else:
        break
print("Missing numbers:")        
for x in pge:
    if i > 25:
        break
    if len(x) < 3:
        if i < int(x):
            while i != int(x):
                print(i)
                i += 1
        i += 1
    else:
        t = x.split('-')
        while i < int(t[0]):
            print(i)
            i += 1
        i = int(t[1]) + 1
