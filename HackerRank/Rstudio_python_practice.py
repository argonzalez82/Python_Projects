#reticulate package already installed 
    #library(reticulate)  
#use the above command to use python in R

    #reticulate::repl_python() 
#use above command to activate the python in the Rstudio Console.

#sample code 

a = "Hello"
b = " World!"

print(a + b)
#run to see all lines output in the console
#source the script to run as .py file and see specific output like 
#print statement. 


import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):

#if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    #Calculations 
    tip = meal_cost / 100 * tip_percent
    
    tax = tax_percent / 100 * meal_cost

    total_cost = meal_cost + tip + tax 

    round(total_cost)		

    print(meal_cost/n, tax/n, total_cost)


    return solve(meal_cost, tip_percent, tax_percent)


solve(100, 20, 7)
