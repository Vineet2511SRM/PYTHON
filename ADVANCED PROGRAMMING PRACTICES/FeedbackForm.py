import tkinter as tk
from tkinter import messagebox
def submit_feedback():
    feedback = feedback_text.get("1.0", "end-1c").strip()
    rating = rating_var.get()
    selected_types = [t for t, v in feedback_types.items() if v.get() == 1]
    
    if not feedback:
        messagebox.showwarning("Empty", "Please enter your feedback before submitting.")
        return
    if not rating:
        messagebox.showwarning("Rating", "Please select a rating before submitting.")
        return

    types_str = ", ".join(selected_types) if selected_types else "None"
    messagebox.showinfo(
        "Thank You",
        f"Feedback submitted successfully!\n\n"
        f"Rating: {rating}⭐\n"
        f"Type: {types_str}\n\n"
        f"Your Feedback:\n{feedback}"
    )

    feedback_text.delete("1.0", "end")
    rating_var.set(0)
    for v in feedback_types.values():
        v.set(0)

root = tk.Tk()
root.title("Feedback Form")
root.geometry("420x480")
root.configure(bg="#f4f6f8")

tk.Label(root, text="🌟 Feedback Form 🌟", font=("Helvetica", 16, "bold"), bg="#f4f6f8", fg="#333").pack(pady=10)

tk.Label(root, text="Rate your experience:", font=("Arial", 12), bg="#f4f6f8").pack(pady=5)
rating_var = tk.IntVar()
rating_frame = tk.Frame(root, bg="#f4f6f8")
rating_frame.pack()
for i in range(1, 6):
    tk.Radiobutton(rating_frame, text=f"{i}⭐", variable=rating_var, value=i, bg="#f4f6f8").pack(side="left", padx=5)

tk.Label(root, text="Type of feedback:", font=("Arial", 12), bg="#f4f6f8").pack(pady=5)
feedback_types = {
    "Bug Report": tk.IntVar(),
    "Suggestion": tk.IntVar(),
    "Appreciation": tk.IntVar(),
}
for t, v in feedback_types.items():
    tk.Checkbutton(root, text=t, variable=v, bg="#f4f6f8").pack(anchor="w", padx=100)

tk.Label(root, text="Enter your feedback:", font=("Arial", 12), bg="#f4f6f8").pack(pady=8)
feedback_text = tk.Text(root, height=8, width=40, font=("Arial", 10))
feedback_text.pack()

tk.Button(root, text="Submit", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", width=15, command=submit_feedback).pack(pady=15)

root.mainloop()