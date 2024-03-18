from tkinter import *
from tkinter import messagebox
import tkinter as tk
import pymysql
from SEM4Project import signin

def user_profile(gmail):  # Pass the 'gmail' parameter here
    # Connect to MySQL
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='falked01',
                                 database='kedaark5',
                                 cursorclass=pymysql.cursors.DictCursor)

    # Fetching data from the database
    with connection:
        with connection.cursor() as cursor:
            # Assuming you have a table named 'users'
            cursor.execute("SELECT Fname, Midname, Lname,age, gmail, mobileno FROM data WHERE gmail = %s", (gmail,))
            result = cursor.fetchone()  # Fetching a single row

            if result:
                fname = result['Fname']
                mname = result['Midname']
                lname = result['Lname']
                gmail = result['gmail']
                phone = result['mobileno']
                age =  result['age'] # Assuming age is hardcoded for now, replace with appropriate value

                # Create the user profile GUI
                app = tk.Tk()
                app.title("User Profile")
                app.geometry("733x500")
                app.configure(bg='#d0bfdf')

                # Labels for displaying user information
                c_name = Label(app, text="Name :", font=20, pady=10, bg='#d0bfdf')
                d_name = Label(app, text="{} {} {}".format(fname, mname, lname), font=20, pady=10, bg='#d0bfdf')

                c_age = Label(app, text="Age :", font=20, pady=10, bg='#d0bfdf')
                d_age = Label(app, text="{}".format(age), font=20, pady=10, bg='#d0bfdf')

                c_email = Label(app, text="Email :", font=20, pady=10, bg='#d0bfdf')
                d_email = Label(app, text="{}".format(gmail), font=20, pady=10, bg='#d0bfdf')

                c_phone = Label(app, text="Phone :", font=20, pady=10, bg='#d0bfdf')
                d_phone = Label(app, text="{}".format(phone), font=20, pady=10, bg='#d0bfdf')

                c_name.pack()
                d_name.pack()
                c_age.pack()
                d_age.pack()
                c_email.pack()
                d_email.pack()
                c_phone.pack()
                d_phone.pack()

                app.mainloop()

            else:
                messagebox.showerror("Error", "User not found")

# Example usage with a Gmail address
# user_profile("{gmail}",)
