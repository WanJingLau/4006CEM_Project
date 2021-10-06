from tkinter import *
from db_conn import readFromDb, insertUpdateDeleteToDb

def change_password():
    global change_password_screen
    global old_password_entry
    global new_password_entry
    global confirm_password_entry
    change_password_screen = Toplevel()

    txt_change_password = "Change Password"
    geometry_size = "1366x768"
    txt_old_password = "Enter old password"
    txt_new_password = "Enter new password"
    txt_confirm_password = "Confirm password"
    txt_save = "Save"

    Label(change_password_screen, text = txt_change_password, font = ("Helvetica", 38, "bold"), foreground = "black").place(x=50, y=95)

    Label(change_password_screen, text = txt_old_password, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=50,y=270)
    old_username_entry = Entry(change_password_screen, font = "Helvetica 12", width=50)
    old_username_entry.place(x=50,y=310)
    Label(change_password_screen, text = txt_new_password, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=50,y=395)
    new_username_entry = Entry(change_password_screen, font = "Helvetica 12", width=50)
    new_username_entry.place(x=50,y=440)
    Label(change_password_screen, text = txt_confirm_password, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=50,y=503)
    confirm_username_entry = Entry(change_password_screen, font = "Helvetica 12", width=50)
    confirm_username_entry.place(x=50,y=540)

    Button(change_password_screen, text= txt_save, font = ("Helvetica", 15, "bold"), foreground="white", background="blue", width=16, height=1, cursor="hand2", command = page_not_found).place(x=587,y=658)

    change_password_screen.title(txt_change_password)
    change_password_screen.geometry(geometry_size)

def page_not_found():
    global page_not_found_screen
    page_not_found_screen = Toplevel(change_password_screen)
    page_not_found_screen.title("Error")
    Label(page_not_found_screen, text="Page not found").pack()
    Button(page_not_found_screen, text="OK", command=delete_page_not_found).pack()

def delete_page_not_found():
    page_not_found_screen.destroy() 