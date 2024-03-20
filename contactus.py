import tkinter as tk


def contactuspage():
    # Create main window
    root = tk.Tk()
    root.title("Contact Us")
    root.geometry("600x500")
    root.configure(bg="#fdc1d0")

    # Content
    content_text = "For any inquiries or feedback regarding the Tax Calculator, please feel free to reach out to us!"
    content_label = tk.Label(root, text=content_text, font=("Arial", 14), bg="#fdc1d0", wraplength=580, justify="left")
    content_label.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10))

    # Further queries message
    further_queries_text = "For further queries, you can contact us at the following:"
    further_queries_label = tk.Label(root, text=further_queries_text, font=("Arial", 14), bg="#fdc1d0")
    further_queries_label.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

    # Phone numbers and emails
    phone1 = "123-456-7890"
    phone2 = "987-654-3210"
    email1 = "info@example.com"
    email2 = "support@example.com"

    # Display phone numbers and emails as text
    phone1_label = tk.Label(root, text="Phone 1:", font=("Arial", 14), bg="#fdc1d0")
    phone1_label.grid(row=2, column=0, padx=(20, 10), pady=5, sticky="e")

    phone1_text = tk.Label(root, text=phone1, font=("Arial", 14), bg="#fdc1d0")
    phone1_text.grid(row=2, column=1, padx=(0, 20), pady=5, sticky="w")

    phone2_label = tk.Label(root, text="Phone 2:", font=("Arial", 14), bg="#fdc1d0")
    phone2_label.grid(row=3, column=0, padx=(20, 10), pady=5, sticky="e")

    phone2_text = tk.Label(root, text=phone2, font=("Arial", 14), bg="#fdc1d0")
    phone2_text.grid(row=3, column=1, padx=(0, 20), pady=5, sticky="w")

    email1_label = tk.Label(root, text="Email 1:", font=("Arial", 14), bg="#fdc1d0")
    email1_label.grid(row=4, column=0, padx=(20, 10), pady=5, sticky="e")

    email1_text = tk.Label(root, text=email1, font=("Arial", 14), bg="#fdc1d0")
    email1_text.grid(row=4, column=1, padx=(0, 20), pady=5, sticky="w")

    email2_label = tk.Label(root, text="Email 2:", font=("Arial", 14), bg="#fdc1d0")
    email2_label.grid(row=5, column=0, padx=(20, 10), pady=5, sticky="e")

    email2_text = tk.Label(root, text=email2, font=("Arial", 14), bg="#fdc1d0")
    email2_text.grid(row=5, column=1, padx=(0, 20), pady=5, sticky="w")

    root.mainloop()
