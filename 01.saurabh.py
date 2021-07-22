# program to choose nay no. from 1 to 6 :
import random 
import os
os.uname()

def generate():
    number = random.randint(1,6)
    print("Dice Rolling Simulator")
    print("Made by saurabh dave")
    if number == 1:
        print("1\n")
    elif number == 2:
        print("2\n")
    elif number == 3:
        print("3\n")
    elif number == 4:
        print("4\n")
    elif number == 5:
        print("5\n")
    elif number == 6:
        print("6\n")
    return

print('To roll again enter "y" \n To exit enter "n"')

while True:
    choice = input()
    if choice == "y" or choice == "Y":
        os.uname()
        generate()
        print('To roll again enter "y"\nTo exit app enter "n"')
    elif choice == "n" or choice == "N":
        os.uname()
        exit()
    else:
        print("Wrong input, try again")





