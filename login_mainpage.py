from tkinter import *
from tkinter.constants import N
from PIL import Image, ImageTk
from register import register
from forget_password import forget_password
from db_conn import readFromDb

def login():
    global login_screen
    global logo
    login_screen = Tk()
    logo = ImageTk.PhotoImage(Image.open("logo.png").resize((80, 80), Image.ANTIALIAS))

    #define text
    txt_login = "Login"
    txt_title = "E-Book System"
    txt_welcome = "Welcome to E-Book System!"
    geometry_size = "1366x768"
    txt_greet = "Hi there! Nice to see you."
    txt_enter = "Please enter your email address and password to access your e-books account."
    txt_email = "Email"
    txt_password = "Password"
    txt_forget_pw  = "Forget your password?"
    txt_register_acc = "No account? Click here to register."
    global email 
    global password
    global email_entry
    global password_entry
    email = StringVar()
    password = StringVar()

    Label(login_screen, image = logo).place(x=649, y=20)
    Label(login_screen, text = txt_welcome, font = ("Helvetica", 14, "bold")).place(x=562, y = 110)
    Label(login_screen, text = txt_login, font = ("Helvetica", 12, "bold")).place(x=80, y=180)
    Label(login_screen, text = txt_greet, font = ("Helvetica", 12)).place(x=80,y=210)
    Label(login_screen, text = txt_enter, font = ("Helvetica", 12, "bold")).place(x=80,y=240)
    Label(login_screen, text = txt_email, font = ("Helvetica", 12, "bold"), foreground = "blue").place(x=80,y=280)
    email_entry = Entry(login_screen, font = "Helvetica 12", textvariable = email, width=50)
    email_entry.place(x=80,y=310)
    Label(login_screen, text = txt_password, font = ("Helvetica", 12, "bold"), foreground = "blue").place(x=80,y=350)
    password_entry = Entry(login_screen,font = "Helvetica 12", textvariable = password, width=50, show= '*')
    password_entry.place(x=80,y=380)
    lbl_forget_pw = Label(login_screen, text = txt_forget_pw, font = ("Helvetica", 12), foreground = "blue", cursor="hand2")
    lbl_forget_pw.place(x=80,y=420)
    lbl_forget_pw.bind("<Button-1>", lambda e: forget_password())
    Button(login_screen, text=txt_login, font = ("Helvetica", 12, "bold"), foreground="white", background="blue", width=20, height=1, cursor="hand2", command = login_verify).place(x=590,y=500)
    lbl_register_acc = Label(login_screen, text = txt_register_acc, font = ("Helvetica", 12), foreground = "blue", cursor="hand2")
    lbl_register_acc.place(x=575,y=550)
    lbl_register_acc.bind("<Button-1>", lambda e: register())

    #login screen
    login_screen.title(txt_title)
    login_screen.geometry(geometry_size)
    login_screen.mainloop()

def login_verify():
    if (len(email.get()) == 0 or len(password.get()) == 0):
        entry_empty()
    else:
        email1 = email.get().lower()
        password1 = password.get()
        email_entry.delete(0, END)
        password_entry.delete(0, END)
    
        dbQuery = "SELECT TOP 1 1 FROM dbo.Users WHERE email = '"+email1+"' AND password_hash = HASHBYTES('SHA2_512', '"+password1+"')"
        
        result = readFromDb(dbQuery)
        if result == None:
            user_password_not_recognised()
        else:
            login_success()

def login_success():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def user_password_not_recognised():
    global user_password_not_recog_screen
    user_password_not_recog_screen = Toplevel(login_screen)
    user_password_not_recog_screen.title("Failed Login")
    Label(user_password_not_recog_screen, text="Wrong Email/ Invalid Password").pack()
    Button(user_password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

 # Designing popup for entry empty
 
def entry_empty():
    global entry_empty_screen
    entry_empty_screen = Toplevel(login_screen)
    entry_empty_screen.title("Failed Login")
    Label(entry_empty_screen, text="Email/ Password is Empty.").pack()
    Button(entry_empty_screen, text="OK", command=delete_entry_empty).pack()

# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy() 
 
def delete_password_not_recognised():
    user_password_not_recog_screen.destroy()

def delete_entry_empty():
    entry_empty_screen.destroy()

login()