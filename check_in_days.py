from tkinter import *
from PIL import Image, ImageTk
from db_conn import insertUpdateBookToDb, readFromDb, insertUpdateDeleteToDb

def check_in_days():
    global check_in_days_screen
    global check_in_days_icon
    #variable declaration
    check_in_days_screen = Toplevel()
    check_in_days_icon = ImageTk.PhotoImage(Image.open("checkin.png").resize((50, 50), Image.ANTIALIAS))
    #text variable declaration
    txt_check_in_days = "Check In Days"
    geometry_size = "1366x768"
    txt_day = "Day1"
    txt_check_in = "Check In"
    txt_hey = "Hey!"
    #screen title,size, maximize windows
    check_in_days_screen.title(txt_check_in_days)
    check_in_days_screen.geometry(geometry_size)
    check_in_days_screen.state("zoomed")
    #page title
    Label(check_in_days_screen, image = check_in_days_icon).place(x=100, y=30)
    Label(check_in_days_screen, text = txt_check_in_days, font = ("Helvetica", 38, "bold"), foreground = "black").place(x=180, y = 20)
    #frame
    Frame(check_in_days_screen, background="white", width=400, height=160).place(x=450, y=220)
    Frame(check_in_days_screen, background="white", width=1270, height=230).place(x=100, y=530)
    #day
    Label(check_in_days_screen, text = txt_day, font = ("Helvetica", 30, "bold"), foreground = "black").place(x=600, y = 270)
    #check in button
    Button(check_in_days_screen, text= txt_check_in, font = ("Helvetica", 12, "bold"), foreground="black", width=20, height=1, cursor="hand2", command = page_not_found).place(x=560,y=420)
    #encourage words
    Label(check_in_days_screen, text = txt_hey, font = ("Helvetica", 16, "bold"), foreground = "black").place(x=130, y = 560)

    check_in_days_screen.title(txt_check_in_days)
    check_in_days_screen.state("zoomed")
    check_in_days_screen.geometry(geometry_size)


def page_not_found():
    global page_not_found_screen
    page_not_found_screen = Toplevel(check_in_days_screen)
    page_not_found_screen.title("Error")
    Label(page_not_found_screen, text="Page not found").pack()
    Button(page_not_found_screen, text="OK", command=delete_page_not_found).pack()

def delete_page_not_found():
    page_not_found_screen.destroy()