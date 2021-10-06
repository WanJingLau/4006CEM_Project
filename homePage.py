from edit_profile import edit_profile
from settings import settings
from tkinter import *
from tkinter.constants import N
from bookcategories import bookcategories
from PIL import Image, ImageTk
from db_conn import readFromDb, insertUpdateDeleteToDb
from store_ebooks import store_ebooks
from upload_ebooks import upload_ebooks

def homepage(email):
    global homepage_screen
    global homepage_icon
    global book_categories_icon
    global store_ebooks_icon
    global upload_ebooks_icon
    global edit_profile_icon
    homepage_screen = Toplevel()
    homepage_icon = ImageTk.PhotoImage(Image.open("homepage.png").resize((65, 65), Image.ANTIALIAS))
    book_categories_icon = ImageTk.PhotoImage(Image.open("bookcategories.png").resize((50, 50), Image.ANTIALIAS))
    store_ebooks_icon = ImageTk.PhotoImage(Image.open("storebooks.png").resize((50, 50), Image.ANTIALIAS))
    upload_ebooks_icon = ImageTk.PhotoImage(Image.open("uploadbooks.png").resize((50, 50), Image.ANTIALIAS))
    edit_profile_icon = ImageTk.PhotoImage(Image.open("profile.png").resize((50, 50), Image.ANTIALIAS))

    txt_homepage = "Home Page"
    txt_logout = "Log Out"
    geometry_size = "1366x768"
    txt_book_categories = "Book Categories"
    txt_store_books = "Store E-books"
    txt_upload_books = "Upload E-books"
    txt_edit_profile = "Edit Profile"

    Button(homepage_screen, text=txt_logout, font = ("Helvetica", 15, "bold"), foreground="black", width=10, height=1, cursor="hand2", command = page_not_found).place(x=1159,y=88)

    Label(homepage_screen, image = homepage_icon).place(x=100, y=40)
    Label(homepage_screen, text = txt_homepage, font = ("Helvetica", 40, "bold"), foreground = "black").place(x=180, y = 40) 
    Label(homepage_screen, image = book_categories_icon).place(x=100, y=200)
    Button(homepage_screen, text=txt_book_categories, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = bookcategories).place(x=200,y=200)
    Label(homepage_screen, image = store_ebooks_icon).place(x=100, y=300)
    Button(homepage_screen, text=txt_store_books, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = store_ebooks).place(x=200,y=300)
    Label(homepage_screen, image = upload_ebooks_icon).place(x=100, y=400)
    Button(homepage_screen, text=txt_upload_books, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = upload_ebooks).place(x=200,y=400)
    Label(homepage_screen, image = edit_profile_icon).place(x=100, y=500)
    Button(homepage_screen, text=txt_edit_profile, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = edit_profile).place(x=200,y=500)

    homepage_screen.title(txt_homepage)
    homepage_screen.geometry(geometry_size)

def page_not_found():
    global page_not_found_screen
    page_not_found_screen = Toplevel(homepage_screen)
    page_not_found_screen.title("Error")
    Label(page_not_found_screen, text="Page not found").pack()
    Button(page_not_found_screen, text="OK", command=delete_page_not_found).pack()

def delete_page_not_found():
    page_not_found_screen.destroy()
