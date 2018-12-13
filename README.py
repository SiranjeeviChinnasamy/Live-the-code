# Live-the-code
#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a #divisor is, it is a number that divides evenly into another number.

X = int(input('Enter a number: '))
New_List = []
for Y in range (1 , X+1): 
  if X%Y == 0:
    New_List.append(Y)
print (New_List)  
