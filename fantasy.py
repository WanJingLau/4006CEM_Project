from tkinter import *
from PIL import Image, ImageTk
from db_conn import readFromDb, insertUpdateDeleteToDb

def fantasy():
    global fantasy_screen
    global back_icon
    fantasy_screen = Toplevel()

    geometry_size = "1366x768"
    txt_fantasy = "Fantasy"
    txt_book_name = "The Shadow of God"
    txt_view_details = "View Details"
    back_icon = ImageTk.PhotoImage(Image.open("back.png").resize((50, 50), Image.ANTIALIAS))
    Button(fantasy_screen, image = back_icon, cursor="hand2", command = close_page).place(x=17,y=65)
    Frame(fantasy_screen, background="light grey", width=1200, height=87).place(x=70, y=242)
    Label(fantasy_screen, text = txt_fantasy, font = ("Helvetica", 38, "bold"), foreground = "black").place(x=100, y=20)
    Label(fantasy_screen, text = txt_book_name, font = ("Helvetica", 25, "bold"), foreground = "black").place(x=106, y=262)
    Button(fantasy_screen, text = txt_view_details, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = page_not_found).place(x=960,y=262)

    fantasy_screen.title(txt_fantasy)
    fantasy_screen.state("zoomed")
    fantasy_screen.geometry(geometry_size)

def page_not_found():
    global page_not_found_screen
    page_not_found_screen = Toplevel(fantasy_screen)
    page_not_found_screen.title("Error")
    Label(page_not_found_screen, text="Page not found").pack()
    Button(page_not_found_screen, text="OK", command=delete_page_not_found).pack()

def delete_page_not_found():
    page_not_found_screen.destroy()

def close_page():
    fantasy_screen.destroy()