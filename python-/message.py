import os
import tkinter as tk
from tkinter import messagebox

# Get the path to the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Folder and file names
folder_name = "Majed"
file_name = "note.txt"

# Full path to the new folder on the desktop
folder_path = os.path.join(desktop_path, folder_name)

# Create the folder (if it doesn't already exist)
os.makedirs(folder_path, exist_ok=True)

# File path inside the folder
file_path = os.path.join(folder_path, file_name)

# Write to the file
with open(file_path, "w") as file:
    file.write("Majed is a Legend")

# Show popup message
root = tk.Tk()
root.withdraw()  # Hide the root window
messagebox.showinfo("Done", "The folder has been created")
messagebox.showinfo("Done", "you been hacked")

print(f"Folder '{folder_name}' created on Desktop with file '{file_name}' containing the text.")
