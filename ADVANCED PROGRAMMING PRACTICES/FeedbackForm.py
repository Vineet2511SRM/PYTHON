import tkinter as tk
from tkinter import messagebox
def submit():
    fb, rate = txt.get("1.0", "end-1c").strip(), rate_var.get()
    types = [t for t, v in types_var.items() if v.get()]
    if not fb: return messagebox.showwarning("Empty", "Enter feedback!")
    if not rate: return messagebox.showwarning("Rating", "Select a rating!")
    messagebox.showinfo("Thank You",
        f"Feedback Submitted!\nRating: {rate}⭐\nType: {', '.join(types) or 'None'}\n\n{fb}")
    txt.delete("1.0", "end"); rate_var.set(0)
    for v in types_var.values(): v.set(0)
root = tk.Tk(); root.title("Feedback Form"); root.geometry("400x450"); root.configure(bg="#f4f6f8")
tk.Label(root, text="🌟 Feedback Form 🌟", font=("Helvetica",16,"bold"), bg="#f4f6f8").pack(pady=10)
rate_var = tk.IntVar()
tk.Label(root, text="Rate your experience:", bg="#f4f6f8").pack()
rf = tk.Frame(root, bg="#f4f6f8"); rf.pack()
for i in range(1,6): tk.Radiobutton(rf, text=f"{i}⭐", variable=rate_var, value=i, bg="#f4f6f8").pack(side="left")
tk.Label(root, text="Type of feedback:", bg="#f4f6f8").pack(pady=5)
types_var = {t: tk.IntVar() for t in ["Bug Report", "Suggestion", "Appreciation"]}
for t,v in types_var.items(): tk.Checkbutton(root, text=t, variable=v, bg="#f4f6f8").pack(anchor="w", padx=90)
tk.Label(root, text="Enter your feedback:", bg="#f4f6f8").pack(pady=5)
txt = tk.Text(root, height=6, width=40); txt.pack()
tk.Button(root, text="Submit", bg="#4CAF50", fg="white", command=submit).pack(pady=10)
root.mainloop()
