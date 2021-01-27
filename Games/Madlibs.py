""" Mad Libs Generator
Command line game, maybe add GUI later,
"""

#creating a GUI for the game.

#tkinter library for GUI's
import tkinter

#Pillow library for images
from PIL import Image, ImageTk

#loads Tkinter into the main gui
main = tkinter.Tk()

#loads the local photo into Python
img = Image.open("/home/CentOS_Laptop/Pictures/photos4editing/2_Dogs_1Kid.jpg")

#loads uploaded image into tkinter
tkimg = ImageTk.PhotoImage(img)

tkinter.Label(main, image=tkimg).pack()
main.mainloop()


#NextStep:
    #Send the .py file to tkinter so game can play in the GUI Window.








#print welcome message.
print()
print()
print()
print('************Ac3NdaMatrix-Games*************')
print()
print()
print("Welcome to a Fun Game of Madlibs")


#Create "While" statement for game where the user
#is asked if they will like to play,
#nest the game code from above in the if statement.


#Loop back to this point once code finishes
player_response = input("Do you want to play, Type Y to play or N to endgame: ")
#player_response.capitalize()
#NextStep:
         #Figure out how to fix capitalization issue.

while (player_response == "Y" or "y"):

#All the questions that the program asks the user
    word1 = input("Choose an animal: ")
    p_noun = input("Choose a plural noun: ")
    noun = input("Choose a family member(i.e. Brother or Uncle: ")
    place = input("Name a place: ")
    adjective = input("Choose an adjective (Describing word): ")
    noun2 = input("Choose a noun: ")
    noun3 = input("Choose another noun: ")
    adjective2 = input("Choose an action word ending in ly:")
    noun4 = input("Choose a flying animal or thing: ")

#Displays the story based on the users input
    print ("------------------------------------------")
    print ("Be kind to your",word1,"-footed",p_noun)
    print ("For a duck may be somebody's",noun,",")
    print ("Be kind to your",p_noun,"in ",place)
    print ("Where the weather is always",adjective,".")
    print ("last but not least wash your ",noun2,",")
    print ("because if you never look up ",adjective2,",")
    print ("Well, you wont see the ",noun3,".")
    print ()
    print ("You may think that is the ",noun4,",")
    print ("Well it is!!")
    print ()
    print ()
    print (":p", "Nicely stated my Friend")
    print ()
    print ()
    print ("------------------------------------------")
    print ()

#NextSteps:
    #create condition loop to keep game running
    #The break below games the game without asking
    #the user if they want to play again figure a
    #way to loop from this point
    break


print("Thanks for playing come again")
print()
print()
print()



#message1 = "Would you like to play a round of Madlibs"
#message2 = "\nType Y to play the game\, Type N to End Game! "


#print(message1 + message2, input())
#list_of_questions
#print(list_to_print)


