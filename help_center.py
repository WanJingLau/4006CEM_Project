from tkinter import *
from PIL import Image, ImageTk
from db_conn import insertUpdateBookToDb, readFromDb, insertUpdateDeleteToDb

def help_center():
    global help_center_screen
    global help_center_icon
    global user_name_entry
    global user_email_address_entry
    global user_question_entry
    #variable declaration
    help_center_screen = Toplevel()
    help_center_icon = ImageTk.PhotoImage(Image.open("helpcenter.png").resize((50, 50), Image.ANTIALIAS))
    user_name = StringVar()
    user_email_address = StringVar()
    user_question = StringVar()
    #text variable declaration
    txt_help_center = "Help Center"
    geometry_size = "1366x768"
    txt_help = "Do you need help?"
    txt_user_name = "Enter Your Name:"
    txt_user_email_address = "Enter Your Email Address:"
    txt_user_question = "Enter Your Question:"
    txt_submit = "Submit"
    #screen title,size, maximize windows
    help_center_screen.title(txt_help_center)
    help_center_screen.geometry(geometry_size)
    help_center_screen.state("zoomed")
    #page title
    Label(help_center_screen, image = help_center_icon).place(x=100, y=30)
    Label(help_center_screen, text = txt_help_center, font = ("Helvetica", 38, "bold"), foreground = "black").place(x=180, y = 20)
    #help
    Label(help_center_screen, text = txt_help, font = ("Helvetica", 12, "bold"), foreground = "black").place(x=80, y = 130)
    #user_name
    Label(help_center_screen, text = txt_user_name, font = ("Helvetica", 12, "bold"), foreground = "blue").place(x=80,y=170)
    user_name_entry = Entry(help_center_screen, textvariable = user_name, font = "Helvetica 12", width=70)
    user_name_entry.place(x=80,y=200)
    user_name_entry.focus_set()
    #user_email_address
    Label(help_center_screen, text = txt_user_email_address, font = ("Helvetica", 12, "bold"), foreground = "blue").place(x=80,y=230)
    user_email_address_entry = Entry(help_center_screen, textvariable = user_email_address, font = "Helvetica 12", width=70)
    user_email_address_entry.place(x=80,y=270)
    user_email_address_entry.focus_set()
    #user_question
    Label(help_center_screen, text = txt_user_question, font = ("Helvetica", 12, "bold"), foreground = "blue").place(x=80,y=310)
    user_question_entry = Entry(help_center_screen, textvariable = user_question, font = "Helvetica 12", width=70)
    user_question_entry.place(x=80,y=340)
    user_question_entry.focus_set()
    #Submit button
    Button(help_center_screen, text= txt_submit, font = ("Helvetica", 12, "bold"), foreground="white", background="blue", width=20, height=1, cursor="hand2", command = page_not_found).place(x=590,y=550)

    help_center_screen.title(txt_help_center)
    help_center_screen.state("zoomed")
    help_center_screen.geometry(geometry_size)


def page_not_found():
    global page_not_found_screen
    page_not_found_screen = Toplevel(help_center_screen)
    page_not_found_screen.title("Error")
    Label(page_not_found_screen, text="Page not found").pack()
    Button(page_not_found_screen, text="OK", command=delete_page_not_found).pack()

def delete_page_not_found():
    page_not_found_screen.destroy()