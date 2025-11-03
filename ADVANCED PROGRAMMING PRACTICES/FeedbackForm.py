import tkinter as tk
from tkinter import messagebox
def submit():
    fb, r = txt.get("1.0","end-1c").strip(), rate.get()
    t = [k for k,v in types.items() if v.get()]
    if not fb: return messagebox.showwarning("Empty","Enter feedback!")
    if not r: return messagebox.showwarning("Rating","Select rating!")
    messagebox.showinfo("Done", f"⭐{r}\n{', '.join(t) or 'None'}\n\n{fb}")
    txt.delete("1.0","end"); rate.set(0)
    [v.set(0) for v in types.values()]
root=tk.Tk(); root.title("Feedback Form"); root.geometry("350x400")
tk.Label(root,text="🌟 Feedback Form 🌟",font=("Arial",14,"bold")).pack(pady=5)
rate=tk.IntVar(); f=tk.Frame(root); f.pack()
for i in range(1,6): tk.Radiobutton(f,text=f"{i}⭐",variable=rate,value=i).pack(side="left")
types={t:tk.IntVar() for t in["Bug","Suggestion","Appreciation"]}
for t,v in types.items(): tk.Checkbutton(root,text=t,variable=v).pack(anchor="w",padx=90)
txt=tk.Text(root,height=5,width=35); txt.pack(pady=5)
tk.Button(root,text="Submit",command=submit).pack(pady=5)
root.mainloop()
