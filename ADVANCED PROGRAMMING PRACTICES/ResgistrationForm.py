import tkinter as tk
from tkinter import messagebox
def submit():
    name, emp_id, dept, desg = name_entry.get(), id_entry.get(), dept_entry.get(), desg_entry.get()
    if not (name and emp_id and dept and desg):
        messagebox.showwarning("Input Error", "Please fill all fields!")
        return
    result_label.config(
        text=f"Employee Details:\nName: {name}\nID: {emp_id}\nDepartment: {dept}\nDesignation: {desg}",
        fg="green"
    )
def reset():
    for entry in (name_entry, id_entry, dept_entry, desg_entry):
        entry.delete(0, tk.END)
    result_label.config(text="")
root = tk.Tk()
root.title("Employee Registration Form")
root.geometry("400x400")
root.resizable(False, False)
tk.Label(root, text="Employee Registration Form", font=("Helvetica", 15, "bold")).pack(pady=10)
fields = ["Employee Name", "Employee ID", "Department", "Designation"]
entries = []
for f in fields:
    tk.Label(root, text=f, font=("Arial", 11)).pack(pady=3)
    e = tk.Entry(root, width=35, font=("Arial", 10))
    e.pack()
    entries.append(e)
name_entry, id_entry, dept_entry, desg_entry = entries
tk.Button(root, text="Submit", bg="#4CAF50", fg="white", width=10, command=submit).pack(pady=10)
tk.Button(root, text="Reset", bg="#f44336", fg="white", width=10, command=reset).pack(pady=5)
result_label = tk.Label(root, text="", font=("Arial", 11))
result_label.pack(pady=15)
root.mainloop()
