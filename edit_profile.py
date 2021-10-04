from tkinter import *
from PIL import Image, ImageTk
from change_password import change_password
from change_username import change_username
from db_conn import readFromDb, insertUpdateDeleteToDb

def edit_profile():
    global edit_profile_screen
    global profile_icon
    edit_profile_screen = Toplevel()
    profile_icon = ImageTk.PhotoImage(Image.open("profile.png").resize((50, 50), Image.ANTIALIAS))

    txt_edit_profile = "Edit Profile"
    geometry_size = "1366x768"
    txt_username = "Change Display Username"
    txt_password = "Change Password"

    Label(edit_profile_screen, image = profile_icon).place(x=100, y=30)
    Label(edit_profile_screen, text = txt_edit_profile, font = ("Helvetica", 38, "bold"), foreground = "black").place(x=180, y = 20)

    Button(edit_profile_screen, text= txt_username, font = ("Helvetica", 25, "bold"), foreground="black", background="light grey", width=60, height=3, cursor="hand2", command = change_username).place(x=101,y=311)
    Button(edit_profile_screen, text= txt_password, font = ("Helvetica", 25, "bold"), foreground="black", background="light grey", width=60, height=3, cursor="hand2", command = change_password).place(x=101,y=498)
 
    edit_profile_screen.title(txt_edit_profile)
    edit_profile_screen.geometry(geometry_size)

def page_not_found():
    global page_not_found_screen
    page_not_found_screen = Toplevel(edit_profile_screen)
    page_not_found_screen.title("Error")
    Label(page_not_found_screen, text="Page not found").pack()
    Button(page_not_found_screen, text="OK", command=delete_page_not_found).pack()

def delete_page_not_found():
    page_not_found_screen.destroy() 