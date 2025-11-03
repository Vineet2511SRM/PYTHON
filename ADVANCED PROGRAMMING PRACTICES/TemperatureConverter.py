import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        val = float(entry.get())
        if choice.get() == 1:
            res = (val * 9/5) + 32
            messagebox.showinfo("Result", f"{val}°C = {res:.2f}°F")
        else:
            res = (val - 32) * 5/9
            messagebox.showinfo("Result", f"{val}°F = {res:.2f}°C")
    except:
        messagebox.showerror("Error", "Enter a valid number!")

root = tk.Tk(); root.title("Temperature Converter"); root.geometry("320x230")
tk.Label(root, text="Temperature Converter", font=("Arial", 13, "bold")).pack(pady=10)
entry = tk.Entry(root, width=25); entry.pack(pady=5)
choice = tk.IntVar(value=1)
tk.Radiobutton(root, text="Celsius → Fahrenheit", variable=choice, value=1).pack()
tk.Radiobutton(root, text="Fahrenheit → Celsius", variable=choice, value=2).pack()
tk.Button(root, text="Convert", command=convert).pack(pady=10)
root.mainloop()
