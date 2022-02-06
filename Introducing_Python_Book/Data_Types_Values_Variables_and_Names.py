# Name              Type        Mutable?        Example                         Chapter

#Boolean            bool        Immutable       True, False                     Chapter 3
#Integer            int         Immutable       47, 25000, 25_000               Chapter 3
#Floating Point     float       Immutable       3.14, 2.7e5                     Chapter 3
#Complex            complex     Immutable       3j, 5 + 9j                      Chapter 22
#Text String        str         Immutable       'alas', 'alack'                 Chapter 5
#List               list        Mutable     ['Winken', 'Bliken','Nod']          Chapter 7
#Tuple              tuple       Immutable       (2,4,8)                         Chapter 7
#Bytes              bytes       Immutable       b'ab\xff'                       Chapter 12
#ByteArray          bytearray   Mutable         bytearray(....)                 Chapter 12
#Set                set         Mutable         set([3,5,7])                    Chapter 8
#Frozen Set         frozenset   Immutable   frozenset(['Elsa', 'Otto'])         Chapter 8
#Dictionary         dict        Mutable    {'game': 'bingo', 'dog': 'dingo',    Chapter 8
#                                           'drummer': 'Ringo'}

 
''' Variables can only contain the following Characters:
    -Lowercase Letters (a through z)
    -Uppercase Letters (A through Z)
    -Digits (0 through 9)
    -Underscore (_)'''


''' The following are keywords in Python or Reserved: These words have special meaning 
    in python code and should not be used for variables. '''


#False      await       else     import     pass
#None       break       except   in         raise
#True       class       finally  is         return
#and        continue    for      lambda     try
#as         def         from     nonlocal   while
#assert     del         global   not        with
#async      elif        if       or         yield


#Working with Assignment (=) sign in Python represents assignement 
#The equation evaluates on the right side and gets assigned to the variable on the left. 

x = 5 
y = x + 12 
print("we have just assigned value 5 to x, \nand 5 + 12 to y")
print("Here is the value for x and y: ", x, y)
print()

#Variables are names not locations of information in memory
#The name just refers to label of the object and datatype 
#determines what the object can hold

a = 99
print
print(type(a))
print()
#a is the label, and it holds the value 99 and it is type integer.

b = a
print(b)
print(type(b))

