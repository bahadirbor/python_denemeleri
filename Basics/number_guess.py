import random
# This program guessing numbers

ceil = int(input("Enter a ceil number: "))
floor = int(input("Enter a floor number :"))

while ceil < floor :
    print("Ceil must be greater than floor!")
    ceil = int(input("Enter a ceil number: "))
    floor = int(input("Enter a floor number :"))

guessing_number = random.randint(floor,ceil)
user_number = int(input("Let's guess a number! :"))

while True:
    if guessing_number == user_number:
        print("Congratulations!")
        break
    elif user_number > guessing_number:
        print("Your number is grater than the number")
        user_number = int(input("Let's guess a number! :"))
    elif user_number < guessing_number:
        print("Your number is less than the number")
        user_number = int(input("Let's guess a number! :"))