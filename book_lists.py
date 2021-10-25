from tkinter import *
from tkinter.font import BOLD
from PIL import Image, ImageTk
import guli

def book_lists():
    global book_lists_screen
    global back_icon
    global action_adventure_icon
    global horror_icon
    global fantasy_icon
    global romance_icon
    global search_icon
    global lbl_image
    global book_lists_title
    book_lists_screen = Toplevel()
    action_adventure_icon = ImageTk.PhotoImage(Image.open("action_adventure_small.png").resize((80, 80), Image.ANTIALIAS))
    romance_icon = ImageTk.PhotoImage(Image.open("romance_small.png").resize((80, 80), Image.ANTIALIAS))
    fantasy_icon = ImageTk.PhotoImage(Image.open("fantasy_small.png").resize((80, 80), Image.ANTIALIAS))
    horror_icon = ImageTk.PhotoImage(Image.open("horror_small.png").resize((80, 80), Image.ANTIALIAS))
    search_icon = ImageTk.PhotoImage(Image.open("search_small.png").resize((80, 80), Image.ANTIALIAS))   
    back_icon = ImageTk.PhotoImage(Image.open("back.png").resize((30, 30), Image.ANTIALIAS))
    #text declaration
    geometry_size = "1366x768"
    book_lists_title = guli.GuliVariable("book_category").get()
    #screen title, size, maximize window
    book_lists_screen.title(book_lists_title)
    book_lists_screen.state("zoomed")
    book_lists_screen.geometry(geometry_size)
    #page title, icon
    lbl_image = Label(book_lists_screen)
    lbl_image.place(x=80, y=40)
    get_page_icon()
    Label(book_lists_screen, text = book_lists_title, font = ("Helvetica", 14, BOLD)).place(x=180, y =70)
    #back button
    Button(book_lists_screen, image = back_icon, cursor="hand2", command = close_page).place(x=15,y=15)


def get_page_icon():
    if book_lists_title == "Action/Adventure":
        lbl_image.config(image=action_adventure_icon)
    elif book_lists_title == "Horror":
        lbl_image.config(image=horror_icon)
    elif book_lists_title == "Fantasy":
        lbl_image.config(image=fantasy_icon)
    elif book_lists_title == "Romance":
        lbl_image.config(image=romance_icon)
    elif book_lists_title == "Search":
        lbl_image.config(image=search_icon)

def close_page():
    book_lists_screen.destroy()