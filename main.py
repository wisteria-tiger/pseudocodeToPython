
from curses.ascii import isdigit
import random
#1
word = input("Enter a string: ")
print(word.upper())

#2
num1 = input("Enter a number: ")
while not num1.isdigit():
    print("Not a valid number.")
    num1 = input("Enter a number: ")
number1 = int(num1)
num2 = input("Enter another number: ")
while not num2.isdigit():
    print("Not a valid number.")
    num2 = input("Enter another number: ")
number2 = int(num2)
sum = number1 + number2
print(f"Sum of numbers: ", sum)

#3
choice = input("Would you like to add numbers together? (y/n): ")
choice.lower()
total = 0 
while choice == "y":
    userInput = input("Enter number to add: ")
    while not userInput.isdigit():
        print("Not a valid number.")
        userInput = input("Enter a number to add: ")
    numToAdd = int(userInput)
    total =+ numToAdd
    choice = input("Would you like to add another number? (y/n): ")

print(total)

#4
flag = True
while flag:
    random.random()
    max = input("Enter a maximum number for a range of random numbers: ")
    while not max.isdigit():
        print("Not a valid number.")
        max = input("Enter a number to add: ")
    maximum = int(max)
    print(random.randint(0, max))
    choice2 = input("Would you like to play again? (y/n): ")
    choice2.lower()
    if choice2 == "n":
        flag = False

#5
evenCount = 0
oddCount = 0
for i in range(10):
    number = random.randint(0, 50)
    if number % 2 == 0:
        evenCount =+ 1
        print("RIGHT")
    else:
        oddCount =+ 1
        print("LEFT")

print(f"RIGHT: ", evenCount)
print(f"LEFT: ", oddCount)