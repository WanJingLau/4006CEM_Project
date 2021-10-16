from tkinter import *
from PIL import Image, ImageTk
from db_conn import readFromDb, insertUpdateDeleteToDb

def romance():
    global romance_screen
    global back_icon
    global romance_icon
    romance_screen = Toplevel()

    geometry_size = "1366x768"
    txt_romance = "Romance"
    txt_book_name = "Will She or Won't She?"
    txt_view_details = "View Details"
    back_icon = ImageTk.PhotoImage(Image.open("back.png").resize((30, 30), Image.ANTIALIAS))
    romance_icon = ImageTk.PhotoImage(Image.open("romance_small.png").resize((80, 80), Image.ANTIALIAS))

    Label(romance_screen, image = romance_icon).place(x=80, y=40)
    Button(romance_screen, image = back_icon, cursor="hand2", command = close_page).place(x=15,y=15)
    Frame(romance_screen, background="light grey", width=1200, height=87).place(x=70, y=242)
    Label(romance_screen, text = txt_romance, font = ("Helvetica", 14, "bold"), foreground = "black").place(x=180, y=70)
    Label(romance_screen, text = txt_book_name, font = ("Helvetica", 12, "bold"), foreground = "black").place(x=106, y=262)
    Button(romance_screen, text = txt_view_details, font = ("Helvetica", 12, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = page_not_found).place(x=960,y=262)

    romance_screen.title(txt_romance)
    romance_screen.state("zoomed")
    romance_screen.geometry(geometry_size)

def page_not_found():
    global page_not_found_screen
    page_not_found_screen = Toplevel(romance_screen)
    page_not_found_screen.title("Error")
    Label(page_not_found_screen, text="Page not found").pack()
    Button(page_not_found_screen, text="OK", command=delete_page_not_found).pack()

def delete_page_not_found():
    page_not_found_screen.destroy()

def close_page():
    romance_screen.destroy()