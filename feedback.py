import tkinter as tk
from tkinter import messagebox

def feedbackform():
    def submit_feedback():
        name = entry_name.get()
        phone = entry_phone.get()
        email = entry_email.get()
        feedback = text_feedback.get("1.0", "end-1c")

        if name.strip() == '' or feedback.strip() == '':
            messagebox.showerror("Error", "Please enter both name and feedback.")
        else:
            messagebox.showinfo("Thank You", f"Thank you {name} for your feedback!")

    # Create main window
    root = tk.Tk()
    root.title("Feedback Page")
    root.geometry("600x500")
    root.configure(bg="#fdc1d0")

    # Create labels with increased font size
    label_name = tk.Label(root, text="Name:", font=("Arial", 12))
    label_name.grid(row=0, column=0, padx=10, pady=10)

    label_phone = tk.Label(root, text="Phone:", font=("Arial", 12))
    label_phone.grid(row=1, column=0, padx=10, pady=10)

    label_email = tk.Label(root, text="Email:", font=("Arial", 12))
    label_email.grid(row=2, column=0, padx=10, pady=10)

    label_feedback = tk.Label(root, text="Feedback:", font=("Arial", 12))
    label_feedback.grid(row=3, column=0, padx=10, pady=10)

    # Create entry boxes with increased font size
    entry_name = tk.Entry(root, font=("Arial", 12))
    entry_name.grid(row=0, column=1, padx=10, pady=10)

    entry_phone = tk.Entry(root, font=("Arial", 12))
    entry_phone.grid(row=1, column=1, padx=10, pady=10)

    entry_email = tk.Entry(root, font=("Arial", 12))
    entry_email.grid(row=2, column=1, padx=10, pady=10)

    # Create text box with increased font size
    text_feedback = tk.Text(root, height=10, width=50, font=("Arial", 12))
    text_feedback.grid(row=3, column=1, padx=10, pady=10)

    # Create submit button
    submit_button = tk.Button(root, text="Submit", command=submit_feedback, font=("Arial", 12))
    submit_button.grid(row=4, columnspan=2, padx=10, pady=10)

    root.mainloop()
