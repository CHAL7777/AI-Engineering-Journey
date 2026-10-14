import random

randnum=random.randint(1,10)
while True:
    inpu=int(input('enter the number: '))

    if randnum<inpu:
        print("Too high")
    elif randnum>inpu:
        print('too low')
    elif randnum==inpu:
        print('you got it')
        break
    else:
        print('enter valid number')