import os
import tkinter as tk
from tkinter import messagebox

filename = "users.txt"

def sign_in():
    username = username_entry.get()
    password = password_entry.get()
    if os.path.exists(filename):
        with open(filename, "r") as file:
            content = file.read()
        if f"{username}:{password}" in content:
            messagebox.showinfo("Success", "✅ Sign in successful!")
        else:
            messagebox.showerror("Error", "❌ Invalid username or password.")
    else:
        messagebox.showerror("Error", "❌ No users found. Please sign up first.")

def sign_up():
    username = username_entry.get()
    password = password_entry.get()
    with open(filename, "a") as file:
        file.write(f"{username}:{password}\n")
    messagebox.showinfo("Success", "✅ Sign up successful!")

# --- GUI Setup ---
root = tk.Tk()
root.title("Login System")
root.geometry("300x200")

# Username
tk.Label(root, text="Username").pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Password
tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Buttons
tk.Button(root, text="Sign In", command=sign_in).pack(pady=5)
tk.Button(root, text="Sign Up", command=sign_up).pack()

root.mainloop()
