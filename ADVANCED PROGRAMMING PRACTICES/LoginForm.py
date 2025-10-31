import tkinter as tk
from tkinter import messagebox

# Function for login validation
def login():
    user = username.get()
    pwd = password.get()

    if user == "admin" and pwd == "1234":
        messagebox.showinfo("Success", f"Welcome, {user}!")
    elif user == "" or pwd == "":
        messagebox.showwarning("Warning", "Please fill in all fields.")
    else:
        messagebox.showerror("Error", "Invalid username or password.")

# Main Window
root = tk.Tk()
root.title("Login Form")
root.geometry("350x250")
root.config(bg="#E8F0FE")  # soft blue background
root.resizable(False, False)

# Frame for the form (centered box)
frame = tk.Frame(root, bg="white", bd=2, relief="groove")
frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=200)

# Title label
tk.Label(frame, text="🔐 User Login", bg="white", fg="#0D47A1", font=("Arial", 16, "bold")).pack(pady=10)

# Username entry
tk.Label(frame, text="Username", bg="white", fg="#333", font=("Arial", 11)).pack(pady=2)
username = tk.Entry(frame, width=28, bd=2, relief="groove")
username.pack(pady=4)

# Password entry
tk.Label(frame, text="Password", bg="white", fg="#333", font=("Arial", 11)).pack(pady=2)
password = tk.Entry(frame, width=28, bd=2, show="*", relief="groove")
password.pack(pady=4)

# Login button
tk.Button(frame, text="Login", command=login, bg="#1565C0", fg="white",
          font=("Arial", 11, "bold"), relief="flat", width=15, pady=3).pack(pady=10)

# Run GUI
root.mainloop()
