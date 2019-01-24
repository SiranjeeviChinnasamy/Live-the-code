#Method1
import random
X = 0
print('Hello what is your name?')
Name = input()
number = random.randint(1,20)
print ("well"+Name+"I'm thinking of number between 1 and 20")
while X<6:
  print ("Take a guess")
  guess = int(input())
  x = x+1
  if guess < number:
    print ("Your guess is low")
  if guess > number:
    print("your guess is high")  
if guess == number:
  X = str(X)    
  print("Good job"+Name+"! ! ")
if guess!= number
  print ("nope:(" "))


#Method 2
import random
X = 0
while repeat:
Name = str(input('Hello what is your name?\n'))
number = random.randint(1,20)
print("guess number from 1 to 20")
Number = int(input())
if Number > number:
  print("It is higher value\n")
if Number < number:
  Number = str(Number)
  print(Number + "Its lower value\n")
if Number == number:
  print("you are right\n")
if Number != number:
  number = str(number)
  print ("the right value is " + number)
