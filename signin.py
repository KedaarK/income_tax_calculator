from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql


def create_sign_in_window():
    def forget_pass():
        def change_password():
            if user_entry.get() == '' or newpass_entry.get() == '' or confirmpass_entry.get() == '':
                messagebox.showerror('Error', 'All Fields are required', parent=window)
            elif newpass_entry.get() != confirmpass_entry.get():
                messagebox.showerror('Error', 'Password and confirm password are not matching', parent=window)
            else:
                con = pymysql.connect(host='localhost', user='root', password='falked01', database='kedaark5')
                mycursor = con.cursor()
                query = 'select * from data where gmail=%s'
                mycursor.execute(query, (user_entry.get()))
                row = mycursor.fetchone()
                if row == None:
                    messagebox.showerror('Error', 'Incorrect email', parent=window)
                else:
                    query = 'update data set password=%s where gmail=%s'
                    mycursor.execute(query, (newpass_entry.get(), user_entry.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo('Success', 'Password is reset, please login with new password')
                    window.destroy()

        window = Toplevel()
        window.title('Change Password')

        bgPic = ImageTk.PhotoImage(file='C:/Users/KEDAAR/Downloads/D7A_35/D7A_35/pythonProject/SEM4Project/background.jpg')

        bgLabel = Label(window, image=bgPic)
        bgLabel.grid()

        heading = Label(window, text='RESET PASSWORD', font=('arial', 18, 'bold'), bg='white', fg='magenta')
        heading.place(x=470, y=60)

        userLabel = Label(window, text='Email', font=('arial', 12, 'bold'), bg='white', fg='orchid1')
        userLabel.place(x=470, y=130)

        user_entry = Entry(window, width=25, fg='magenta', font=('arial', 11, 'bold'), bd=0)
        user_entry.place(x=470, y=160)

        Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=180)

        newpassLabel = Label(window, text='New Password', font=('arial', 12, 'bold'), bg='white', fg='orchid1')
        newpassLabel.place(x=470, y=210)

        newpass_entry = Entry(window, width=25, fg='magenta', font=('arial', 11, 'bold'), bd=0)
        newpass_entry.place(x=470, y=240)

        Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=260)

        confirmpassLabel = Label(window, text='Confirm Password', font=('arial', 12, 'bold'), bg='white', fg='orchid1')
        confirmpassLabel.place(x=470, y=290)

        confirmpass_entry = Entry(window, width=25, fg='magenta', font=('arial', 11, 'bold'), bd=0)
        confirmpass_entry.place(x=470, y=320)

        Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=340)

        submitButton = Button(window, text='Submit', font=('Open Sans', 16, 'bold'), fg='white', bg='firebrick1',
                              activebackground='white', cursor='hand2', bd=0, width=19, command=change_password)
        submitButton.place(x=470, y=390)
        window.mainloop()

    def login_user():
        if emailEntry.get() == '' or passwordEntry.get() == '':
            messagebox.showerror('Error', 'All Fields are required')
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='falked01')
                mycursor = con.cursor()
            except:
                messagebox.showerror('Error', 'Connection is not established try again')
                return
            query = 'use kedaark5'
            mycursor.execute(query)
            query = 'Select  * from username=%s and password=%s'
            mycursor.execute(query, (emailEntry.get(), passwordEntry.get()))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error', 'Invalid username or password')
            else:
                messagebox.showinfo('Welcome', 'Login successful')

    def user_enter(event):
        if emailEntry.get() == 'Email':
            emailEntry.delete(0, END)

    def password_enter(event):
        if passwordEntry.get() == 'Password':
            passwordEntry.delete(0, END)

    def hide():
        openeye.config(file='C:/Users/KEDAAR/Downloads/D7A_35/D7A_35/pythonProject/SEM4Project/closeye.png')
        passwordEntry.config(show='*')
        eyeButton.config(command=show)

    def show():
        openeye.config(file='C:/Users/KEDAAR/Downloads/D7A_35/D7A_35/pythonProject/SEM4Project/openeye.png')
        passwordEntry.config(show='')
        eyeButton.config(command=hide)

    # GUI

    login_window = Tk()

    login_window.geometry('990x660+50+50')
    login_window.resizable(0, 0)
    login_window.title('Login Page')
    bgImg = ImageTk.PhotoImage(file='C:/Users/KEDAAR/Downloads/D7A_35/D7A_35/pythonProject/SEM4Project/bg.jpg')

    bgLabel = Label(login_window, image=bgImg)
    bgLabel.place(x=0, y=0)

    heading = Label(login_window, text='USER LOGIN', font=('Microsoft Yahei UI Light', 23, 'bold'), bg='white',
                    fg='firebrick1')
    heading.place(x=605, y=120)

    emailEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
    emailEntry.place(x=580, y=200)
    emailEntry.insert(0, 'Email')

    emailEntry.bind('<FocusIn>', user_enter)

    Frame(login_window, width=250, height=2, bg='firebrick1').place(x=580, y=222)

    passwordEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
    passwordEntry.place(x=580, y=260)
    passwordEntry.insert(0, 'Password')

    passwordEntry.bind('<FocusIn>', password_enter)

    Frame(login_window, width=250, height=2, bg='firebrick1').place(x=580, y=282)
    openeye = PhotoImage(file='openeye.png')
    eyeButton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2',
                       command=hide)
    eyeButton.place(x=800, y=255)

    forgetButton = Button(login_window, text='Forget Password?', bd=0, bg='white', fg='firebrick1',
                          activebackground='white', cursor='hand2', font=('Microsoft Yahei UI Light', 9, 'bold'),
                          activeforeground='firebrick1', command=forget_pass)
    forgetButton.place(x=715, y=295)

    loginButton = Button(login_window, text='Login', font=('Open Sans', 16, 'bold'), fg='white', bg='firebrick1',
                         activebackground='white', cursor='hand2', bd=0, width=19, command=login_user)
    loginButton.place(x=578, y=350)
    '''orlabel = label(login_window,text='---------',font=('Open Sans',16),fg='firebrick1')
    orlabel.place(x=583, y= )'''

    signuplabel = Label(login_window, text='Dont have an account?', font=('Open Sans', 9, 'bold'), fg='firebrick1',
                        bg='white')
    signuplabel.place(x=590, y=400)

    newaccountButton = Button(login_window, text='Create new one', font=('Open Sans', 9, 'bold underline'), fg='blue',
                              bg='white', activebackground='blue', cursor='hand2', bd=0)
    newaccountButton.place(x=727, y=400)

    login_window.mainloop()

#create_sign_in_window()
