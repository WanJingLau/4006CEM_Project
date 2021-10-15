from tkinter import *
from PIL import Image, ImageTk
from db_conn import readFromDb, insertUpdateDeleteToDb

def horror():
    global horror_screen
    global back_icon
    horror_screen = Toplevel()

    geometry_size = "1366x768"
    txt_horror = "Horror"
    txt_book_name = "Last Things"
    txt_view_details = "View Details"
    back_icon = ImageTk.PhotoImage(Image.open("back.png").resize((50, 50), Image.ANTIALIAS))
    Button(horror_screen, image = back_icon, cursor="hand2", command = close_page).place(x=17,y=65)

    Frame(horror_screen, background="light grey", width=1200, height=87).place(x=70, y=242)
    Label(horror_screen, text = txt_horror, font = ("Helvetica", 38, "bold"), foreground = "black").place(x=100, y=20)
    Label(horror_screen, text = txt_book_name, font = ("Helvetica", 25, "bold"), foreground = "black").place(x=106, y=262)
    Button(horror_screen, text = txt_view_details, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = page_not_found).place(x=960,y=262)

    horror_screen.title(txt_horror)
    horror_screen.state("zoomed")
    horror_screen.geometry(geometry_size)

def page_not_found():
    global page_not_found_screen
    page_not_found_screen = Toplevel(horror_screen)
    page_not_found_screen.title("Error")
    Label(page_not_found_screen, text="Page not found").pack()
    Button(page_not_found_screen, text="OK", command=delete_page_not_found).pack()

def delete_page_not_found():
    page_not_found_screen.destroy()

def close_page():
    horror_screen.destroy()