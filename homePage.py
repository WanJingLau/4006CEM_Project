from delete_ebooks import delete_ebooks
from edit_ebooks import edit_ebooks
from edit_profile import edit_profile
from settings import settings
from tkinter import *
from tkinter.constants import N
from bookcategories import bookcategories
from PIL import Image, ImageTk
from db_conn import readFromDb
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
    homepage_icon = ImageTk.PhotoImage(Image.open("homepage.png").resize((80, 80), Image.ANTIALIAS))
    book_categories_icon = ImageTk.PhotoImage(Image.open("bookcategories.png").resize((50, 50), Image.ANTIALIAS))
    store_ebooks_icon = ImageTk.PhotoImage(Image.open("storebooks.png").resize((50, 50), Image.ANTIALIAS))
    upload_ebooks_icon = ImageTk.PhotoImage(Image.open("uploadbooks.png").resize((50, 50), Image.ANTIALIAS))
    edit_profile_icon = ImageTk.PhotoImage(Image.open("profile.png").resize((50, 50), Image.ANTIALIAS))
    #text variable declaration
    txt_homepage = "Home Page"
    txt_logout = "Log Out"
    geometry_size = "1366x768"
    txt_book_categories = "Book Categories"
    txt_store_books = "Store E-books"
    txt_upload_books = "Upload E-books"
    txt_edit_profile = "Edit Profile"
    #homepage title, size, maximize window
    homepage_screen.title(txt_homepage)
    homepage_screen.state("zoomed")
    homepage_screen.geometry(geometry_size)
    #logout button
    Button(homepage_screen, text=txt_logout, font = ("Helvetica", 12, "bold"), foreground="black", width=10, height=1, cursor="hand2", command = logout).place(x=730,y=145)
    #homepage icon, title
    Label(homepage_screen, image = homepage_icon).place(x=80, y=40)
    Label(homepage_screen, text = txt_homepage, font = ("Helvetica", 14, "bold"), foreground = "black").place(x=180, y = 70) 
    #book category
    Label(homepage_screen, image = book_categories_icon).place(x=80, y=230)
    Button(homepage_screen, text=txt_book_categories, font = ("Helvetica", 12, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = bookcategories).place(x=180,y=240)
    #edit profile
    Label(homepage_screen, image = edit_profile_icon).place(x=550, y=230)
    Button(homepage_screen, text=txt_edit_profile, font = ("Helvetica", 12, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = edit_profile).place(x=650,y=240)
    #store ebook
    Label(homepage_screen, image = store_ebooks_icon).place(x=80, y=330)
    Button(homepage_screen, text=txt_store_books, font = ("Helvetica", 12, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = store_ebooks).place(x=180,y=340)
    #upload ebook
    Label(homepage_screen, image = upload_ebooks_icon).place(x=550, y=330)
    Button(homepage_screen, text=txt_upload_books, font = ("Helvetica", 12, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = upload_ebooks).place(x=650,y=340)

    #check if is admin, show edit & delete ebook
    show_lbl(email)

def page_not_found():
    global page_not_found_screen
    page_not_found_screen = Toplevel(homepage_screen)
    page_not_found_screen.title("Error")
    Label(page_not_found_screen, text="Page not found").pack()
    Button(page_not_found_screen, text="OK", command=delete_page_not_found).pack()

def show_lbl(email):
    dbQuery = """SELECT R.Name, U.username
                 FROM dbo.Users U WITH(NOLOCK)
                 INNER JOIN dbo.UserRole UR WITH(NOLOCK) ON UR.UserId = U.Id
                 INNER JOIN dbo.Roles R WITH(NOLOCK) ON R.Id = UR.RoleId
                 WHERE U.email = '"""+email+"""'"""
    
    result = readFromDb(dbQuery)
    global editebooks_icon
    global deleteebooks_icon
    txt_edit_ebooks = "Edit E-Books"
    txt_delete_ebooks = "Delete E-Books"
    editebooks_icon = ImageTk.PhotoImage(Image.open("editebooks.png").resize((50, 50), Image.ANTIALIAS))
    deleteebooks_icon = ImageTk.PhotoImage(Image.open("deleteebooks.png").resize((50, 50), Image.ANTIALIAS))
    if result[0] == "admin":
        #edit ebook
        Label(homepage_screen, image = editebooks_icon).place(x=80, y=430)
        Button(homepage_screen, text = txt_edit_ebooks, font = ("Helvetica", 12, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = edit_ebooks).place(x=180,y=440)
        #delete ebook
        Label(homepage_screen, image = deleteebooks_icon).place(x=550, y=430)
        Button(homepage_screen, text = txt_delete_ebooks, font = ("Helvetica", 12, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = delete_ebooks).place(x=650,y=440)
    Label(homepage_screen, text = "Hi, " + result[1] + ". Welcome back!", font = ("Helvetica", 12, "bold")).place(x=80, y=150)
def delete_page_not_found():
    page_not_found_screen.destroy()

def logout():
    homepage_screen.destroy()