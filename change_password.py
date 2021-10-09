from tkinter import *
from db_conn import readFromDb, insertUpdateDeleteToDb

def change_password():
    global change_password_screen
    global old_password_entry
    global new_password_entry
    global confirm_password_entry
    global old_password
    global new_password
    global confirm_new_password
    change_password_screen = Toplevel()
    txt_change_password = "Change Password"
    geometry_size = "1366x768"
    txt_old_password = "Enter old password"
    txt_new_password = "Enter new password"
    txt_confirm_password = "Confirm password"
    txt_save = "Save"
    old_password = StringVar()
    new_password = StringVar()
    confirm_new_password = StringVar()


    Label(change_password_screen, text = txt_change_password, font = ("Helvetica", 38, "bold"), foreground = "black").place(x=50, y=95)

    Label(change_password_screen, text = txt_old_password, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=50,y=270)
    old_password_entry = Entry(change_password_screen, font = "Helvetica 12", width=50, textvariable = old_password, show= '*')
    old_password_entry.place(x=50,y=310)

    Label(change_password_screen, text = txt_new_password, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=50,y=395)
    new_password_entry = Entry(change_password_screen, font = "Helvetica 12", textvariable = new_password, width=50, show= '*')
    new_password_entry.place(x=50,y=440)
    Label(change_password_screen, text = txt_confirm_password, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=50,y=503)
    confirm_password_entry = Entry(change_password_screen, font = "Helvetica 12", width=50, textvariable = confirm_new_password, show= '*')
    confirm_password_entry.place(x=50,y=540)

    Button(change_password_screen, text= txt_save, font = ("Helvetica", 15, "bold"), foreground="white", background="blue", width=16, height=1, cursor="hand2", command = password_verify(email)).place(x=587,y=658)

    change_password_screen.title(txt_change_password)
    change_password_screen.geometry(geometry_size)

def password_verify():
    if len(old_password.get()) == 0:
        entry("Old Password is empty. Please enter old password.")
    elif len(new_password.get()) == 0:
        entry("New Password is empty. Please enter new password.")
    elif len(confirm_new_password.get()) == 0:
        entry("Confirm Password is empty. Please enter confirm password.")
    elif new_password.get() != confirm_new_password.get():
        entry("New Password and Confirm Password not matched. Please reenter password.")
    else:
        dbQuery = """SELECT TOP 1 1 FROM dbo.Users WITH(NOLOCK) 
                     WHERE email = '"""+email+"""' 
                     AND password_hash = HASHBYTES('SHA2_512', '"""+old_password+"""')"""
        
        result = readFromDb(dbQuery)
        if result == None:
            entry("Wrong old password provided. Please reenter password.")
        else:
            dbQuery1 = """UPDATE dbo.Users
                          SET password_hash = HASHBYTES('SHA2_512', '"""+new_password+"""')
                          WHERE email = '"""+email+"""'"""
            result1 = insertUpdateDeleteToDb(dbQuery1)
            if result1 == 1:
                change_pw_success()
                return
            
            entry("Change password failed. Please retry.")

def change_pw_success():
    global change_pw_screen
    change_pw_screen = Toplevel(change_password_screen)
    change_pw_screen.title("Success")
    Label(change_pw_screen, text="Change Password Successfully").pack()
    Button(change_pw_screen, text="OK", command=delete_pw_screen).pack()

def delete_pw_screen():
    change_pw_screen.destroy()
    change_password_screen.destroy()

def entry(entry):
    global entry_screen
    entry_screen = Toplevel(change_password_screen)
    entry_screen.title("Failed Change Password")
    Label(entry_screen, text=entry).pack()
    Button(entry_screen, text="OK", command=delete_entry_screen).pack()

def delete_entry_screen():
    entry_screen.destroy()
