import tkinter as tk
from tkinter import messagebox
from itertools import cycle
import time
from SEM4Project import signin,sign_up2


# Define functions for menu actions
def home_action():
    print("Going to Home")


def tax_rules_action():
    print("Viewing Tax Rules")


def contact_us_action():
    print("Contacting Us")


def feedback_action():
    messagebox.showinfo("Feedback", "Thank you for your feedback! Please sign in to submit feedback.")


def sign_up_action():
    sign_up2.create_sign_up_window()


def log_in_action():
    signin.create_sign_in_window()
    # messagebox.showinfo("Log In", "Redirecting to Log In Page...")


# Function to animate images
def animate_images(canvas, image_list):
    image_cycle = cycle(image_list)  # Create an iterator to cycle through images
    label = tk.Label(canvas)
    label.pack()

    while True:
        for image_file in image_cycle:
            # Load the image
            image = tk.PhotoImage(file=image_file)

            # Calculate the dimensions of the image frame
            frame_width = canvas.winfo_width()
            frame_height = canvas.winfo_height()

            # Resize the image to fit within the frame
            resized_image = image.subsample(4)  # Increase the subsampling factor to make images larger

            # Update the label with the resized image
            label.configure(image=resized_image)
            label.image = resized_image  # Retain reference to the image to prevent garbage collection

            canvas.update()
            time.sleep(2)  # Change image every 2 seconds


def create_window():
    # Create main window
    window = tk.Tk()
    window.title("Tax Management System")
    window.geometry("600x500")
    window.configure(bg='#d0bfdf')  # Set background color

    # Add information label
    info_label = tk.Label(window, text="Welcome to the Tax Management System!", bg='#d0bfdf', fg='black',
                          font=("Eurostile Bold", 14))
    info_label.pack(pady=45)

    # Add label for tax importance
    tax_info_text = """Taxes play a crucial role in funding government activities and services. They contribute to the development of infrastructure, education, healthcare, and various public welfare programs. Paying taxes ensures the smooth functioning of society by providing essential services and benefits to all citizens."""
    tax_label = tk.Label(window, text=tax_info_text, bg="white", fg="black", font=("Calisto MT", 11),
                         wraplength=500)
    tax_label.pack()

    # Create menu bar
    menubar = tk.Menu(window, bg='#7e5c83')  # Set background color

    # Create menu items with direct commands
    menubar.add_command(label="HOME", command=home_action)
    menubar.add_command(label="TAX RULES", command=tax_rules_action)
    menubar.add_command(label="CONTACT US", command=contact_us_action)

    # Create a Feedback submenu
    feedback_menu = tk.Menu(menubar, tearoff=0, bg='#7e5c83', fg='white')  # Set background and foreground color
    feedback_menu.add_command(label="Submit Feedback", command=feedback_action)

    # Add Feedback submenu to the menu bar
    menubar.add_cascade(label="FEEDBACK", menu=feedback_menu)

    # Create a Sign In submenu
    sign_menu = tk.Menu(menubar, tearoff=0, bg='#7e5c83', fg='white')  # Set background and foreground color
    sign_menu.add_command(label="Sign Up", command=sign_up_action)
    sign_menu.add_command(label="Log In", command=log_in_action)

    # Add Sign In submenu to the menu bar
    menubar.add_cascade(label="SIGN", menu=sign_menu)

    # Configure the main window to use the menu bar
    window.config(menu=menubar)

    # Create frame for image transition
    image_frame_width = window.winfo_width() // 4  # 1/4th of window width
    image_frame_height = 200  # Fixed height
    image_frame = tk.Frame(window, width=image_frame_width, height=image_frame_height, bg="white")
    image_frame.pack(side=tk.BOTTOM, pady=20)

    # Create canvas within the frame to display images
    canvas = tk.Canvas(image_frame, bg="white", width=image_frame_width, height=image_frame_height)
    canvas.pack()

    # List of image file names
    image_list = [
        "wf1.png",
        "wf2.png",
        "wf3.png",
        "wf4.png",
        "wf5.png"
    ]

    try:
        # Start animation
        animate_images(canvas, image_list)
    except Exception as e:
        print("An error occurred:", e)

    window.mainloop()

if __name__ == "__main__":
    create_window()
