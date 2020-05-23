print('Die Rolling simulator')
from random import randint

a = input('Enter P/p to roll the Die or Q/q quit the game :' )
if a.capitalize() == 'P':
    print(randint(1,6))
elif a.capitalize() == 'Q':
    exit()
while True:
    a = input('Enter P/p to roll the Die again or Q/q quit the game :' )
    if a.capitalize() == 'P':
        print(randint(1,6))
    elif a.capitalize() == 'Q':
        exit()
