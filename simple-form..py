import tkinter as tk
from tkinter import messagebox

# Submit button ka function 
def submit():
    name = entry_name.get()
    age = entry_age.get()
    password = entry_password.get()
    bio = text_bio.get("1.0", tk.END)  # Text area 

    info = f"Name: {name}\nAge: {age}\nPassword: {password}\nBio: {bio}"
    messagebox.showinfo("Submitted Info", info)

# Main Window k liye
root = tk.Tk()
root.title("User Form")
root.geometry("400x400")

# Name input
tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root, width=30)
entry_name.pack()

# Age input
tk.Label(root, text="Age:").pack()
entry_age = tk.Entry(root, width=30)
entry_age.pack()

# Password input
tk.Label(root, text="Password:").pack()
entry_password = tk.Entry(root, width=30, show="*")
entry_password.pack()

# Text Area (Bio / Extra Info) input
tk.Label(root, text="Bio / About You:").pack()
text_bio = tk.Text(root, width=30, height=5)
text_bio.pack()

# Submit Button 
tk.Button(root, text="Submit", command=submit).pack(pady=10)

root.mainloop()
