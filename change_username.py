from tkinter import *
from db_conn import readFromDb, insertUpdateDeleteToDb

def change_username():
    global change_username_screen
    global old_username_entry
    global new_username_entry
    change_username_screen = Toplevel()

    txt_change_username = "Change Display Username"
    geometry_size = "1366x768"
    txt_old_username = "Enter old username"
    txt_new_username = "Enter new username"
    txt_save = "Save"

    Label(change_username_screen, text = txt_change_username, font = ("Helvetica", 38, "bold"), foreground = "black").place(x=50, y=95)

    Label(change_username_screen, text = txt_old_username, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=50,y=270)
    old_username_entry = Entry(change_username_screen, font = "Helvetica 12", width=50)
    old_username_entry.place(x=50,y=310)
    Label(change_username_screen, text = txt_new_username, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=50,y=395)
    new_username_entry = Entry(change_username_screen, font = "Helvetica 12", width=50)
    new_username_entry.place(x=50,y=440)

    Button(change_username_screen, text= txt_save, font = ("Helvetica", 15, "bold"), foreground="white", background="blue", width=16, height=1, cursor="hand2", command = page_not_found).place(x=587,y=658)

    change_username_screen.title(txt_change_username)
    change_username_screen.geometry(geometry_size)

def page_not_found():
    global page_not_found_screen
    page_not_found_screen = Toplevel(change_username_screen)
    page_not_found_screen.title("Error")
    Label(page_not_found_screen, text="Page not found").pack()
    Button(page_not_found_screen, text="OK", command=delete_page_not_found).pack()

def delete_page_not_found():
    page_not_found_screen.destroy() 