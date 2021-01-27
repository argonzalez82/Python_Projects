#Website - https://www.hackinscience.org/exercises/comparisons

#Instructions:
#Find the biggest value in a given list.
#Try it by using only a temporary variable, a for loop, and #an if to compare
#the values. I prefilled the list in the answer box.

#Challenge Code Below:

##*************************************##

#Create a list with the provided values.
the_list = [
    143266561,
    1738152473,
    312377936,
    1027708881,
    1495785517,
    1858250798,
    1693786723,
    1871655963,
    374455497,
    430158267,
]

#Code Algorithm based on constraints listed. 

#I need a for loop with a temp. variable that iterates throught the_list 

for num in the_list:
    if num == max(the_list):   #If statement that will compare 
        print(num)             #each item in the_list to the max  
                               #and print out the largest(max).

