#from curses.ascii import isdigit
import random

print("hello")

myvariable = 5

def myfunction(x, y):
    return (x + y)

print(myfunction(myvariable, 10))

mylist = [1,2,3,4,5,"bot"]

print(mylist[0])

for x in mylist:
    print(x)

#1
word = input("Enter a string: ")
print(word.upper())

#2
num1 = int(input("Enter a number: "))
#while not isdigit:
  #  print("Not a valid number.")
  #  num1 = input("Enter a number: ")

num2 = int(input("Enter another number: "))
#while not isdigit:
   # print("Not a valid number.")
   # num2 = input("Enter another number: ")

sum = num1 + num2
print(f"Sum of numbers: ", {sum})

#3

choice = input("Would you like to add numbers together? (y/n): ")
total = 0
while choice == "y":
    numToAdd = int(input("Enter number to add: "))
    total = total + numToAdd
    choice = input("Would you like to add another number? (y/n): ")

print(total)

#4
flag = True
while flag:
    random.random()
    max = int(input("Enter a maximum number for a range of random numbers: "))
    print(random.randint(0, max))
    choice2 = input("Would you like to play again? (y/n): ")
    if choice2 == "n":
        flag = False

#5
evenCount = 0
oddCount = 0
for i in range(10):
    number = random.randint(0, 50)
    if number % 2 == 0:
        evenCount = evenCount + 1
        print("RIGHT")
    else:
        oddCount = oddCount + 1
        print("LEFT")

print(f"RIGHT: ", evenCount)
print(f"LEFT: ", oddCount)