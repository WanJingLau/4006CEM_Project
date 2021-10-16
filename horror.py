from tkinter import *
from PIL import Image, ImageTk
from db_conn import readFromDb, insertUpdateDeleteToDb

def horror():
    global horror_screen
    global back_icon
    global horror_icon
    horror_screen = Toplevel()

    geometry_size = "1366x768"
    txt_horror = "Horror"
    txt_book_name = "Last Things"
    txt_view_details = "View Details"
    back_icon = ImageTk.PhotoImage(Image.open("back.png").resize((30, 30), Image.ANTIALIAS))
    horror_icon = ImageTk.PhotoImage(Image.open("horror_small.png").resize((80, 80), Image.ANTIALIAS))

    Label(horror_screen, image = horror_icon).place(x=80, y=40)
    Button(horror_screen, image = back_icon, cursor="hand2", command = close_page).place(x=15,y=15)
    Frame(horror_screen, background="light grey", width=1200, height=87).place(x=70, y=242)
    Label(horror_screen, text = txt_horror, font = ("Helvetica", 14, "bold"), foreground = "black").place(x=180, y=70)
    Label(horror_screen, text = txt_book_name, font = ("Helvetica", 12, "bold"), foreground = "black").place(x=106, y=262)
    Button(horror_screen, text = txt_view_details, font = ("Helvetica", 12, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = page_not_found).place(x=960,y=262)

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