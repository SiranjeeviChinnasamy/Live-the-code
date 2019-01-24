#1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
#Code
List = []
for i in range(1500,2701):
 if i%7==0 and i%5==0:
  List.append(i)
print(List)

#2. Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
#[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ] 
#Code
Temp =  int(input("Enter Temperature in Celcius : \n"))
Fahrenheit = (9/5)*Temp+32
print("{0} F".format(Fahrenheit))

#3. Write a Python program to guess a number between 1 to 9. Go to the editor
#Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, 
#user will get a "Well guessed!" message, and the program will exit.
import random
Num, Guess = random.randint(1,9),0
while Num!=Guess:
 Guess = int(input("Enter the Number between 1 to 9)
print("well Guessed")                   
