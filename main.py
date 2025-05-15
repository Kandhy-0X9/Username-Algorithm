import random
from faker import Faker
fake = Faker()

#welcome the user

print("Welcome User\n")

#ask the user for his/her name

name_E = input("What is your name? ").lower().replace(" ", "_")
print()

choice = input(" Do you want to use your real name? (Yes or No)").strip().lower()
print()

#create if statement 

if choice == "yes":
    randomNumber = str(random.randint(0, 100))
    print(name_E+randomNumber)
    print()

elif choice == "no":   
    Print = fake.name().lower().replace(" ", "_")
    randomNumber2 = str(random.randint(0, 100))
    print(Print+randomNumber2)
    print()
