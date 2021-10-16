from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from db_conn import readFromDb, insertUpdateDeleteToDb

def change_username():
    global change_username_screen
    global change_username_image
    global old_username_entry
    global new_username_entry
    global username
    global back_icon
    change_username_screen = Toplevel()
    txt_change_username = "Change Display Username"
    geometry_size = "1366x768"
    txt_old_username = "Current username"
    txt_new_username = "Enter new username"
    txt_save = "Save"
    username = StringVar()
    back_icon = ImageTk.PhotoImage(Image.open("back.png").resize((30, 30), Image.ANTIALIAS))
    change_username_image = ImageTk.PhotoImage(Image.open("change_username_image.png").resize((260, 170), Image.ANTIALIAS))
    Button(change_username_screen, image = back_icon, cursor="hand2", command = close_page).place(x=15,y=15)
    Label(change_username_screen, image = change_username_image).place(x=1100, y=590)

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
    change_username_screen.state("zoomed")
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
    messagebox.showinfo("Success", "Change Username Successfully", parent = change_username_screen)
    change_username_screen.destroy()

def entry(entry):
    messagebox.showerror("Failed Change Username", entry, parent = change_username_screen)

def close_page():
    change_username_screen.destroy()