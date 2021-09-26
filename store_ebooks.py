from tkinter import *
from PIL import Image, ImageTk
from db_conn import readFromDb, insertUpdateDeleteToDb

def store_ebooks():
    global store_ebooks_screen
    global store_ebooks_icon
    global delete_icon

    store_ebooks_screen = Toplevel()
    store_ebooks_icon = ImageTk.PhotoImage(Image.open("storebooks.png").resize((50, 50), Image.ANTIALIAS))
    delete_icon = ImageTk.PhotoImage(Image.open("delete.png").resize((50, 50), Image.ANTIALIAS))

    txt_store_ebooks = "Store E-books"
    geometry_size = "1366x768"
    txt_storage = "This is the storage of at least more than 20 e-books."
    txt_list = "Lists(2/20)"
    txt_book_name = "Will She or Won't She?"
    txt_author = "by Sheila Norton"
    txt_edition = "Edition last updated December 1, 2006"
    txt_remove = "Remove this item?"
    txt_read = "Read"
    txt_book2_name = "Percy Jackson"
    txt_author2 = "by Rick Riordan"
    txt_edition2 = "Edition last updated March 18, 2016"

    Label(store_ebooks_screen, image = store_ebooks_icon).place(x=100, y=30)
    Label(store_ebooks_screen, text = txt_store_ebooks, font = ("Helvetica", 38, "bold"), foreground = "black").place(x=180, y = 20)
    
    Label(store_ebooks_screen, image = delete_icon).place(x=952, y=336)
    Label(store_ebooks_screen, image = delete_icon).place(x=952, y=601)
    Button(store_ebooks_screen, text= txt_read, font = ("Helvetica", 15, "bold"), foreground="blue", width=16, height=1, cursor="hand2", command = page_not_found).place(x=952,y=406)
    Button(store_ebooks_screen, text= txt_read, font = ("Helvetica", 15, "bold"), foreground="blue", width=16, height=1, cursor="hand2", command = page_not_found).place(x=952,y=665)
    Label(store_ebooks_screen, text = txt_remove, font = ("Helvetica", 15), foreground = "black").place(x=1016, y=355)
    Label(store_ebooks_screen, text = txt_remove, font = ("Helvetica", 15), foreground = "black").place(x=1016, y=620)

    Label(store_ebooks_screen, text = txt_storage, font = ("Helvetica", 15), foreground = "black").place(x=60, y=152)
    Label(store_ebooks_screen, text = txt_list, font = ("Helvetica", 15), foreground = "blue").place(x=70, y=226)
    
    Label(store_ebooks_screen, text = txt_book_name, font = ("Helvetica", 20, "bold"), foreground = "black").place(x=258, y=336)
    Label(store_ebooks_screen, text = txt_author, font = ("Helvetica", 15), foreground = "black").place(x=258, y=400)
    Label(store_ebooks_screen, text = txt_edition, font = ("Helvetica", 15), foreground = "black").place(x=258, y=438)

    Label(store_ebooks_screen, text = txt_book2_name, font = ("Helvetica", 20, "bold"), foreground = "black").place(x=272, y=584)
    Label(store_ebooks_screen, text = txt_author2, font = ("Helvetica", 15), foreground = "black").place(x=272, y=646)
    Label(store_ebooks_screen, text = txt_edition2, font = ("Helvetica", 15), foreground = "black").place(x=272, y=684)

    store_ebooks_screen.title(txt_store_ebooks)
    store_ebooks_screen.geometry(geometry_size)

def page_not_found():
    global page_not_found_screen
    page_not_found_screen = Toplevel(store_ebooks_screen)
    page_not_found_screen.title("Error")
    Label(page_not_found_screen, text="Page not found").pack()
    Button(page_not_found_screen, text="OK", command=delete_page_not_found).pack()

def delete_page_not_found():
    page_not_found_screen.destroy()