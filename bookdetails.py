from tkinter import *
from PIL import Image, ImageTk
from db_conn import readFromDb, insertUpdateDeleteToDb

def bookdetails():
    global book_details_screen
    global book_categories_icon
    global search_entry
    global Book1_icon
    global fourstar_icon

    book_details_screen = Toplevel()
    Book1_icon = ImageTk.PhotoImage(Image.open("Book1.png").resize((180, 220), Image.ANTIALIAS))
    fourstar_icon = ImageTk.PhotoImage(Image.open("fourstar.png").resize((160, 70), Image.ANTIALIAS))
    book_categories_icon = ImageTk.PhotoImage(Image.open("bookcategories.png").resize((50, 50), Image.ANTIALIAS))

    txt_book_details = "Book Details"
    txt_search = "Search"
    geometry_size = "1366x768"
    txt_read = "Read"
    txt_store = "Store"
    txt_review = "Review"
    txt_edition = "An edition of Percy Jackson - Tome 3(2016)"
    txt_last_edited = "Last edited by March 18, 2021"
    txt_book_name = "Percy Jackson - Tome 3"
    txt_author = "by Rick Riordan"
    txt_marks = "4.45   -   90 Ratings   -   120 Currently reading   -   138 Have read"
    txt_published = "This edition was published in 2016 by Poche Jeunesse. Written in English-389 pages"
    txt_description = "Monsters always kill demigods. Percy and his friends Annabeth, Grover and Talia find themselves facing a terrible Mantis."
    txt_read_more = "Read more"

    search_entry = Entry(book_details_screen, font = "Helvetica 15", textvariable = txt_search, width=50)
    search_entry.place(x=100,y=90) 
    Button(book_details_screen, text=txt_search, font = ("Helvetica", 15, "bold"), foreground="black", width=10, height=1, cursor="hand2", command = page_not_found).place(x=700,y=80)
    Label(book_details_screen, image = book_categories_icon).place(x=100, y=30)
    Label(book_details_screen, text = txt_book_details, font = ("Helvetica", 38, "bold"), foreground = "black").place(x=180, y = 20)
    
    Label(book_details_screen, image = Book1_icon).place(x=56, y=149)
    Label(book_details_screen, text = txt_edition, font = ("Helvetica", 15), foreground = "black").place(x=298, y=163)
    Label(book_details_screen, text = txt_last_edited, font = ("Helvetica", 15), foreground = "black").place(x=1051, y=163)
    Label(book_details_screen, text = txt_book_name, font = ("Helvetica", 21, "bold")).place(x=279, y=205)
    Label(book_details_screen, text = txt_author, font = ("Helvetica", 15), foreground = "blue").place(x=298, y=286)
    Label(book_details_screen, image = fourstar_icon).place(x=297, y=350)
    Label(book_details_screen, text = txt_marks, font = ("Helvetica", 15)).place(x=493, y=350)
    Label(book_details_screen, text = txt_published, font = ("Helvetica", 15)).place(x=297, y=430)
    Label(book_details_screen, text = txt_description, font = ("Helvetica", 15, )).place(x=307, y=499)
    Label(book_details_screen, text = txt_read_more, font = ("Helvetica", 15), foreground = "blue").place(x=307, y=603)

    Button(book_details_screen, text= txt_read, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = page_not_found).place(x=307,y=655)
    Button(book_details_screen, text= txt_store, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = page_not_found).place(x=646,y=655)
    Button(book_details_screen, text= txt_review, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = page_not_found).place(x=978,y=655)

    book_details_screen.title(txt_book_details)
    book_details_screen.geometry(geometry_size)


def page_not_found():
    global page_not_found_screen
    page_not_found_screen = Toplevel(book_details_screen)
    page_not_found_screen.title("Error")
    Label(page_not_found_screen, text="Page not found").pack()
    Button(page_not_found_screen, text="OK", command=delete_page_not_found).pack()

def delete_page_not_found():
    page_not_found_screen.destroy()