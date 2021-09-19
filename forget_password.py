import random
import smtplib
from tkinter import *
from tkinter.constants import N
from PIL import Image, ImageTk
from db_conn import readFromDb, insertUpdateDeleteToDb
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def forget_password():
    global forget_pw_screen
    global forget_pw_icon
    forget_pw_screen = Toplevel()
    forget_pw_icon = ImageTk.PhotoImage(Image.open("forget_password.png").resize((80, 80), Image.ANTIALIAS))

    #define text
    txt_forget_pw = "Forget Password?"
    txt_provide = "Please provide your email address to reset your password."
    txt_email = "Enter your email address"
    txt_submit = "Submit"
    txt_title = "E-Book System"
    geometry_size = "1366x768"

    global email
    global email_entry
    email = StringVar()

    Label(forget_pw_screen, image = forget_pw_icon).place(x=570, y=40)
    Label(forget_pw_screen, text = txt_forget_pw, font = ("Helvetica", 14, "bold")).place(x=660, y = 70)
    Label(forget_pw_screen, text = txt_provide, font = ("Helvetica", 12, "bold")).place(x=80, y = 200)
    Label(forget_pw_screen, text = txt_email, font = ("Helvetica", 12, "bold"), foreground = "blue").place(x=80, y = 260) 
    email_entry = Entry(forget_pw_screen, font = "Helvetica 12", textvariable = email, width=50)
    email_entry.place(x=80,y=290)
    email_entry.focus_set()
    Button(forget_pw_screen, text=txt_submit, font = ("Helvetica", 12, "bold"), foreground="white", background="blue", width=20, height=1, cursor="hand2", command = reset_verify).place(x=590,y=500) 
    
    forget_pw_screen.title(txt_title)
    forget_pw_screen.geometry(geometry_size)

def reset_verify():
    if len(email.get()) == 0:
        entry("Email address is empty. Please enter an email address.")
    else:
        dbQuery = "SELECT TOP 1 1 FROM dbo.Users WHERE email = '"+email.get().lower()+"'"
        result = readFromDb(dbQuery)
        if result == None:
            email_entry.delete(0, END)
            entry("Email address not found. Please re-enter your email address.")
        else:
            reset_password()

def entry(entry):
    global entry_screen
    entry_screen = Toplevel(forget_pw_screen)
    entry_screen.title("Failed Reset")
    Label(entry_screen, text=entry).pack()
    Button(entry_screen, text="OK", command=delete_entry_screen).pack()

def delete_entry_screen():
    entry_screen.destroy()

def reset_password():
    email_info = email.get().lower()
    new_pw = pw_generator()
    dbQuery = """UPDATE dbo.Users 
                 SET password_hash = HASHBYTES('SHA2_512', '"""+new_pw+"""') 
                 WHERE email = '"""+email_info+"""'"""
    
    result = insertUpdateDeleteToDb(dbQuery)
    if result == 1:
        email_entry.delete(0, END)
        send_email(email_info, new_pw)
        reset_success()
    else:
        entry("Reset failed. Please try again.")

def pw_generator():
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
    password =""

    for i in range(0, 8):
        password = password + random.choice(digits)
    return password

def send_email(email, password):
    sender_email = "ebook4006@gmail.com" 
    sender_password = "ebookwjwc"
    dbQuery = "SELECT username FROM dbo.Users WHERE email = '"+email+"'"
    username = readFromDb(dbQuery)
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = email
    message["Subject"] = "RESET PASSWORD FOR E-BOOK ACCCOUNT" 
    email_body_info = """Hi """+username[0]+""",

Reset Password Successfully. You may login with your new password.

Your new password: """+password+""" 


Thanks.


***** THIS IS AN AUTOMATED EMAIL. DO NOT REPLY *****"""

    message.attach(MIMEText(email_body_info, 'plain'))

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender_email,sender_password)
    server.sendmail(sender_email,email,message.as_string())
    server.quit()

def reset_success():
    global reset_success_screen
    reset_success_screen = Toplevel(forget_pw_screen)
    reset_success_screen.title("Success")
    Label(reset_success_screen, text="""Password reset success. 
    An email has been sent. Kindly check your email.""").pack()
    Button(reset_success_screen, text="OK", command=delete_reset_success).pack()

def delete_reset_success():
    reset_success_screen.destroy()
    delete_forget_pw_screen()

def delete_forget_pw_screen():
    forget_pw_screen.destroy()