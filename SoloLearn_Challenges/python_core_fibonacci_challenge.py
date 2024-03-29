#Python Core Fibonacci Challenge

'''The Fibonacci sequence is one of the most famous formulas in mathematics.
Each number in the sequence is the sum of the two numbers that precede it.
For example, here is the Fibonacci sequence for 10 numbers, starting from 
0: 0,1,1,2,3,5,8,13,21,34.

Write a program to take N (variable num in code template) positive numbers 
as input, and recursively calculate and output the first N numbers of the
Fibonacci sequence (starting from 0).

Sample Input
6

Sample Output
0
1
1
2
3
5

If you are making the Fibonacci sequence for n numbers, 
you should use n<=1 condition as the base case.'''


num = int(input())

def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))


# check if the number of terms is valid
if num <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(num):
       print(fibonacci(i))