print('Finding armstrong numbers in given range')
print('Enter the lower limit a')
a = int(input())
print('Enter the upper limit b')
b = int(input())
for i in range(a, b + 1):
    c = i
    num = 0
    n = 0
    while c != 0: 
        c = c//10
        n += 1
    c = i
    while c != 0:
        num += pow(c % 10, n)
        c = c//10
    if(num == i):
        print(i)    