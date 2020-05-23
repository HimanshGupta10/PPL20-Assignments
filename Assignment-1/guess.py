from random import randint

print('Guessing the correct number'.capitalize())
a = randint(1,100)
print('Guess a number')
arr = []
arr.append(int(input()))
if(arr[0] == a):
    print('You have guessed the correct number. You Won!!!')
    exit()
if(abs(a - arr[0]) < 10):
    print('Warm... Guess again')
else:
    print('Cold... Guess again')       
while True:
    arr.append(int(input()))
    if(arr[-1] == a):
        print('You have guessed the correct number. You Won!')
        exit()
    elif(abs(a - arr[-1]) > abs(a -arr[-2])):
        print('Colder!... Guess again')
    else:
        print('Warmer!... Guess again')    
