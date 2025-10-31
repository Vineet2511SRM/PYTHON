import tkinter as tk
from tkinter import messagebox

def register():
    name = name_entry.get()
    email = email_entry.get()
    if name and email:
        messagebox.showinfo("Success", f"Registered {name} with email {email}")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields")

root = tk.Tk()
root.title("Registration Form")
root.geometry("350x250")

tk.Label(root, text="Full Name").pack(pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.pack()

tk.Label(root, text="Email").pack(pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.pack()

tk.Button(root, text="Register", command=register).pack(pady=15)
root.mainloop()
