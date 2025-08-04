import tkinter as tk

#main window
window = tk.Tk()

window.geometry("1920x1080")
window.title("Title")
# ✅ Get full screen size
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# ✅ Set window to full screen size
window.geometry(f"{screen_width}x{screen_height}")
# ✅ Disable resizing
window.resizable(False, False)



# create a label for username
username_label = tk.Label(window, text="Username:")
username_label.pack(pady=(10, 10))

username_entry = tk.Entry(window)
username_entry.pack(pady=5)


age_label = tk.Label(window, text="Age: ")
age_label.pack(pady=(10, 10))

age_entry = tk.Entry(window)
age_entry.pack(pady=5)

#Error message
display_label = tk.Label(window, text="")
display_label.pack(pady=5)

def save_user_info():
    #get the username
    username = username_entry.get().strip()
    age = age_entry.get().strip()

    #make sure the filed is not empty
    if not username or not age:
        display_label.config(text="Please Fill in the empty field")
        return
    
    if not age.isdigit():
        display_label.config(text="Age must be a number")
        return
    
    if int(age) > 100:
        display_label.config(text="age must be under 100")
        return
    
    normalized_username = username.lower()

    # Read all existing usernames from the file
    try:
        with open("username.txt", "r") as file:
            existing_username = []

            for line in file:
                parts = line.strip().split('|')
                if parts and "Username:" in parts[0]:
                    name = parts[0].split("Username:")[1].strip().lower()
                    existing_username.append(name)
    except FileNotFoundError:
        existing_username = []

    #check if the username already exists
    if normalized_username in existing_username:
        display_label.config(text=f"the Username '{username}' been taken")
    else:
        #save it
        with open("username.txt", "a") as file:
            file.write(f"Username: {username} | Age: {age}\n")
        display_label.config(text=f"Done! thanks {username}")

    #to clear the input after submiting
    username_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

#To save the username



save_username = tk.Button(window, text="Submit", command=save_user_info)
save_username.pack(pady=5)

window.mainloop()