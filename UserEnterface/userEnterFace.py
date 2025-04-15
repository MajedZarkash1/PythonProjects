from tkinter import *

def change_bg_color():
    current_color = main.cget("bg")
    new_color = "gray" if current_color == "black" else "black"
    main.config(background=new_color)

    current_color_label = username.cget("bg")
    new_color_label = "gray" if current_color_label == "black" else "black"
    username.config(background=new_color_label)
    
    current_color_label = title.cget("bg")
    new_color_label = "gray" if current_color_label == "black" else "black"
    title.config(background=new_color_label)
    
    current_color_label = password.cget("bg")
    new_color_label = "gray" if current_color_label == "black" else "black"
    password.config(background=new_color_label)



main = Tk()

main.geometry("500x500")
main.title("UserEnterFace")
main.config(background="black")

bg_button = Button(main,
                   text="Change Color",
                   command=change_bg_color,
                   font=('solid', 10),
                   bg="gray",
                   fg="white")
bg_button.place(x=10,y=10)

title = Label(main, 
              text="Welcome",
              font=('Solid',14),
              fg='white',
              bg='black',
              )

username = Label(main, 
              text="Username:",
              font=('Solid',14),
              fg='white',
              bg='black',
              )

entryUsername = Entry(main,
              width=10,)

password = Label(main, 
                text="Password:",
                font=('Solid',14),
                fg='white',
                bg='black',)

enteryPassword = Entry(main,
                       width=10,
                       show="*")

submit = Button(main,
                text="submit",
                font=('solid', 12),
                relief="solid",
                bd=1,
                activebackground='white'
                )

title.pack(pady=25)
username.pack()
entryUsername.pack() 
password.pack()
enteryPassword.pack()
submit.pack(pady=20)

main.mainloop()