from tkinter import *

window = Tk() #this to hold the TK to use it later in the code

window.geometry("500x700") #this for width and height of the window

window.title("Transater") #this is the title

icon = PhotoImage(file='T.png') #this to import the image
window.iconphoto(True,icon) #this to display the image as an icon

window.config(background="white") #this to change the color of the background

#this is the title you can enter a text by using Lable
title = Label(window,
               text="Welcome", #text
               font=('Lucida Console',20,), #font
               fg='black', #text's color
               padx=50, #gap X
               pady=10,) #gap Y

#this for making input make sure to use ENRTY()
input = Entry()
#here is for the disegn
input.config(
    fg='black',
    font=('Lucida Console',10,),
    bg='#F2F3F5')

#this is the defult text
#input.insert(0, 'type . . .')

#input.config(state=DISABLED) #the input ACTIVE/DISABLED

input.config(width=25)# manage the size

#input.config(show='*') #for password


input.pack()


title.pack() # this with the name if the var of Label will display the text
#title.place() #this if you want to change the place of the text #and the above will be in the center

window.mainloop() #this will display the window , and listen to the events

