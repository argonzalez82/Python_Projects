#open file with book titles.
file = open("/usercode/files/books.txt", "r")

#use readlines() to turn the file content to a list. 
book_list = file.readlines()
file.close()

#list of titles to split and apply uppercase
s_list = book_list

#duplicate list of titles for count of char
c_list = book_list

#using list comp. to count char of book titles and place in new list
counted_list = [len(i) - i.count('\n') for i in c_list]


#create new list of just the first letter from each item
cap_list = [i.upper() for i in s_list]

#combine both list to achieve the required output of "first letter of title
#and total count of characters from the book title using a for loop.

i = 0                #variable to iterate through counted_list indexes
for c in cap_list:
    print(c[0],end="")
    print(counted_list[i]) 
    while i < len(counted_list):
        i += 1
        break






******************************************************************************************************************************************************************************************************************************************************************

#input of book titles
book_list = ["Yoohoo", "Harry Potter", "The Hobbit"]



#Sample Solution using Functions. 


def list_count(x):
    for i in x:
        char_count = len(i) - i.count('\n')
        char_list = char_count
        char_list.append(i)
    return char_list

#list.append(item)

#Create function that will go thru list and store the first Letter. 

def first_letter(x):
    for i in  x:
        caps = split(i.upper())   
        caps = caps[0]


list_count(cool_list)
first_letter(cool_list)


print(caps + char_count)