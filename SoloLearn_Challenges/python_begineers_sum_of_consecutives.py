#Instructions:
'''Sum of Consecutive Numbers


No one likes homework, but your math teacher has given you an assignment 
to find the sum of the first N numbers.
Let’s save some time by creating a program to do the calculation for you!

Take a number N as input and output the sum of all numbers from 1 to N 
(including N).

Sample Input
100

Sample Output
5050

Explanation: The sum of all numbers from 1 to 100 is equal to 5050.'''

#You can iterate over a range and calculate the 
#sum of all numbers in the range.
#Remember, range(a, b) does not include b, thus you 
#need to use b+1 to include b in the range.



N = int(input("Please input an integer : "))

item = range(1, N + 1)
for i in item:
    sum = 0
    for j in range(1, i + 1):
        sum = sum + j
print(str(sum))


N = int(input())

i = range(0, (N + 1))
sum = 0 

while N >= i:
    sum = sum + i
    i += 1
print(sum)    