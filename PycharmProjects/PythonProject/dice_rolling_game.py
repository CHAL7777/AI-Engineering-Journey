import random

choice = input('Do you wanna roll the die (y/n) ').lower()

while True:
    if choice=='y':
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        print(dice1,dice2)
        sec=input('')
    elif choice=='n':
        print('thank you playing')
        break
    else:
        print("enter valid value what have you asked ")