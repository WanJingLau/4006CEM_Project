from tkinter import *
from PIL import Image, ImageTk
from db_conn import readFromDb, insertUpdateDeleteToDb

def store_ebooks():
    global store_ebooks_screen
    global store_ebooks_icon

    store_ebooks_screen = Toplevel()
    store_ebooks_icon = ImageTk.PhotoImage(Image.open("storebooks.png").resize((50, 50), Image.ANTIALIAS))

    txt_store_ebooks = "Store E-books"
    geometry_size = "1366x768"
    txt_storage = "This is the storage of at least more than 20 e-books."
    txt_book_name = "Percy Jackson - Tome 3"
    txt_author = "by Rick Riordan"
    txt_read = "Read"
    txt_download = "Download"
    txt_delete = "Delete"

    Label(store_ebooks_screen, image = store_ebooks_icon).place(x=100, y=30)
    Label(store_ebooks_screen, text = txt_store_ebooks, font = ("Helvetica", 38, "bold"), foreground = "black").place(x=180, y = 20)
    
    Button(store_ebooks_screen, text= txt_read, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = page_not_found).place(x=784,y=261)
    Button(store_ebooks_screen, text= txt_download, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = page_not_found).place(x=946,y=261)
    Button(store_ebooks_screen, text= txt_delete, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = page_not_found).place(x=1106,y=261)

    Label(store_ebooks_screen, text = txt_storage, font = ("Helvetica", 15), foreground = "black").place(x=60, y=152)    
    Label(store_ebooks_screen, text = txt_book_name, font = ("Helvetica", 20, "bold"), foreground = "black").place(x=106, y=261)
    Label(store_ebooks_screen, text = txt_author, font = ("Helvetica", 15), foreground = "black").place(x=482, y=261)

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