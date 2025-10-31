import tkinter as tk
from tkinter import messagebox

def submit_feedback():
    feedback = feedback_text.get("1.0", "end-1c")
    if feedback.strip():
        messagebox.showinfo("Thank You", "Feedback submitted successfully!")
    else:
        messagebox.showwarning("Empty", "Please enter your feedback before submitting.")

root = tk.Tk()
root.title("Feedback Form")
root.geometry("400x300")

tk.Label(root, text="Enter your feedback:", font=("Arial", 12)).pack(pady=10)
feedback_text = tk.Text(root, height=8, width=40)
feedback_text.pack()

tk.Button(root, text="Submit", command=submit_feedback).pack(pady=15)
root.mainloop()
