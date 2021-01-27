#Webiste - https://www.hackinscience.org/exercises/counting-words


#Instructions:
#Provide a script that prints the number of words in the given paragraph.

#I prefilled the answer box with the paragraph, in a variable below. 
#Advice
#Take a look at the split method.

#Challenge Code Below:

##***************************##

phantom_menace = """Turmoil has engulfed the Galactic Republic. 
The taxation of trade routes to outlying star systems is in
dispute. Hoping to resolve the matter with a blockade of deadly
battleships, the greedy Trade Federation has stopped all shipping to
the small planet of Naboo. While the congress of the Republic
endlessly debates this alarming chain of events, the Supreme
Chancellor has secretly dispatched two Jedi Knights, the guardians of
peace and justice in the galaxy, to settle the conflict"""

# Enter your code below:

#Create a new empty list
#Take the above story and use the split() method to break into individual words
#Save the words from the split into the empty list
new_list = []
new_list = phantom_menace.split()


#use len() to count the words(indexes) in the list save to a new variable. 
#print the length variable 
#print the list for fun  
counting_words = len(new_list)
print(counting_words)
print(new_list)
