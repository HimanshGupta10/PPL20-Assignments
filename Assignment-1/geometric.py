print('Finding first 10 numbers of geometric series')
print('Enter base a and common factor r')
a = int(input())
b = int(input())
print(a)
for i in range(1, 10):
    print(a*pow(b,i))
