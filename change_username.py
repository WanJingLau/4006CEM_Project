from tkinter import *
from db_conn import readFromDb, insertUpdateDeleteToDb

def change_username():
    global change_username_screen
    global old_username_entry
    global new_username_entry
    global username
    change_username_screen = Toplevel()
    txt_change_username = "Change Display Username"
    geometry_size = "1366x768"
    txt_old_username = "Current username"
    txt_new_username = "Enter new username"
    txt_save = "Save"
    username = StringVar()

    Label(change_username_screen, text = txt_change_username, font = ("Helvetica", 38, "bold"), foreground = "black").place(x=50, y=95)
    Label(change_username_screen, text = txt_old_username, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=50,y=270)
    old_username_entry = Entry(change_username_screen, font = "Helvetica 12", width=50, state='disabled')
    old_username_entry.place(x=50,y=310)
    old_username_entry.insert(0, getCurrentUsername(email))
    Label(change_username_screen, text = txt_new_username, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=50,y=395)
    new_username_entry = Entry(change_username_screen, font = "Helvetica 12", width=50, textvariable=username)
    new_username_entry.place(x=50,y=440)
    Button(change_username_screen, text= txt_save, font = ("Helvetica", 15, "bold"), foreground="white", background="blue", width=16, height=1, cursor="hand2", command = username_verify(email)).place(x=587,y=658)
    change_username_screen.title(txt_change_username)
    change_username_screen.geometry(geometry_size)

def getCurrentUsername():
    dbQuery = """SELECT username FROM dbo.Users WITH(NOLOCK) WHERE email = '"""+email+"""'"""
    result = readFromDb(dbQuery)
    return result[0]

def username_verify():
        if len(username.get()) == 0:
            entry("New username is empty. Please enter username")
        else:
            dbQuery = """UPDATE dbo.Users
                         SET username = '"""+username.get()+"""'
                         WHERE email = '"""+email+"""'"""
            result1 = insertUpdateDeleteToDb(dbQuery)
            if result1 == 1:
                change_username_success()
                return
            
            entry("Change username failed. Please retry.")

def change_username_success():
    global change_username1_screen
    change_username1_screen = Toplevel(change_username_screen)
    change_username1_screen.title("Success")
    Label(change_username1_screen, text="Change Username Successfully").pack()
    Button(change_username1_screen, text="OK", command=delete_username_screen).pack()

def delete_username_screen():
    change_username1_screen.destroy()
    change_username_screen.destroy()

def entry(entry):
    global entry_screen
    entry_screen = Toplevel(change_username_screen)
    entry_screen.title("Failed Change Username")
    Label(entry_screen, text=entry).pack()
    Button(entry_screen, text="OK", command=delete_entry_screen).pack()

def delete_entry_screen():
    entry_screen.destroy()