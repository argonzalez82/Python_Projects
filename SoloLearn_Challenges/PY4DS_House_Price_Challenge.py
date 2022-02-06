#House Prices Instructions. 
''' You are given an array that represents house prices.
Calculate and output the percentage of houses that are within one standard 
deviation from the mean.

To calculate the percentage, divide the number of houses 
that satisfy the condition by the total number of houses, 
and multiply the result by 100.'''


import numpy as np

data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000,
230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])
#Calculate Standard deviation and mean
data_std = np.std(data)
data_mean = np.mean(data)

#Calculate standard deviation range.
std_range_neg = (data_mean - data_std)
std_range_pos = (data_mean + data_std)
std_range_neg = round(std_range_neg, 3)
std_range_pos = round(std_range_pos, 3)

full_range = []

for i in data:
    if i > std_range_neg and i < std_range_pos:
        full_range.append(i)

np.array(full_range)
data_average =  np.sum(full_range) / len(full_range)

print(data_average)