#Website - https://www.hackinscience.org/exercises/powers-of-two

#Instructions:
#Print the 10 first powers of two (beware: not the first squares!)
#Start at 0, so the first power of two is 2**0 (which happen to be one), followed
#by 2**1, 2**2, and so on up to 2**3.

#As a reminder, the power operator in Python is written **, so:

#Example 
print("Example code of 2 ** 5 = ",2 ** 5) #Evaluates to 32 

#Challenge Code Below:
##***************************##

#variable is assigned the value 2 
num = 2

#create a range for the powers of the variable
#from 0 - 10
#range(0,10)

#output the result of the range using a for loop and print

for i in range(0,10):
    print(num ** i)