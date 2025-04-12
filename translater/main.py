from tkinter import *

window = Tk() #this to hold the TK to use it later in the code

window.geometry("500x700") #this for width and height of the window

window.title("ChangeColor") #this is the title appear on the top

icon = PhotoImage(file='T.png') #this to import the image
window.iconphoto(True,icon) #this to display the image as an icon
#--------------------------------------------------------------------#
colors = ["gray", "yellow", "white", "green", "red", "brown"]
current_color = 0 #this will track the index of the current color

def change_color():
    global current_color # to import the var here

    window.config(background=colors[current_color])
    current_color = (current_color +1) % len(colors) # LOOP back to first color

#To change the text background's color
def text_color():
    global current_color

    title2.config(background=colors[current_color])
    current_color = (current_color +1) % len(colors)

def button_color():
    global current_color

    button3.config(background=colors[current_color])
    current_color = (current_color +1) % len(colors)


'''
#this is the title you can enter a text by using Lable
welcome = Label(window,
               text="Welcome", #text
               font=('Lucida Console',20,), #font
               fg='black', #text's color
               padx=50, #gap X
               pady=10,) #gap Y

welcome.config(background='white')
welcome.pack() # this with the name if the var of Label will display the text
#welcome.place() #this if you want to change the place of the text #and the above will be in the center
'''

title2 = Label(window,
                    text="Click to Change the color", 
                    font=('Lucida Console', 23,),
                    padx=50,
                    pady=10,)

title2.config(background='white')
title2.pack()


window.config(background="white") #this to change the color of the background

#button
button = Button(window,
                text="Main background",
                font=('Lucida Console', 12),
                bg="#AED6F1",
                fg="black",
                width=20,
                height=5,
                activebackground='#C5C6D0',
                command=change_color) #listener 

button.config(background='gray')
button.pack(pady=20)

button2 = Button(window,
                text="text's background",
                font=('Lucida Console', 12),
                bg="#AED6F1",
                fg="black",
                width=20,
                height=5,
                relief="solid",
                activebackground='#C5C6D0',
                command=text_color)

button2.config(background='gray')
button2.pack(pady=20)

button3 = Button(window,
                text="text's background",
                font=('Lucida Console', 12),
                bg="#AED6F1",
                fg="black",
                width=20,
                height=5,
                relief="solid", #border
                bd=1, #border size
                command=button_color)

button3.config(background='gray')
button3.pack(pady=20)

'''
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
'''
window.mainloop() #this will display the window , and listen to the events

