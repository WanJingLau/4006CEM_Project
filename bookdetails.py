from comment import comment
from review import review
from store_ebooks import store_ebooks
from tkinter import *
from PIL import Image, ImageTk
from db_conn import readFromDb, insertUpdateDeleteToDb

def bookdetails():
    global book_details_screen
    global book_categories_icon
    global fourstar_icon
    global back_icon

    book_details_screen = Toplevel()
    fourstar_icon = ImageTk.PhotoImage(Image.open("fourstar.png").resize((160, 70), Image.ANTIALIAS))
    book_categories_icon = ImageTk.PhotoImage(Image.open("bookcategories.png").resize((50, 50), Image.ANTIALIAS))
    back_icon = ImageTk.PhotoImage(Image.open("back.png").resize((30, 30), Image.ANTIALIAS))

    txt_book_details = "Book Details"
    geometry_size = "1366x768"
    txt_read = "Read"
    txt_store = "Store"
    txt_review = "Review"
    txt_comment = "View Comment"
    txt_book_name = "Book Name: Percy Jackson - Tome 3"
    txt_author = "Author - Rick Riordan"
    txt_marks = "4.45"
    txt_summary = "Summary: Monsters always kill demigods. Percy and his friends Annabeth, Grover and Talia find themselves facing a terrible Mantis."
    
    Button(book_details_screen, image = back_icon, cursor="hand2", command = close_page).place(x=15,y=15)

    Label(book_details_screen, image = book_categories_icon).place(x=100, y=30)
    Label(book_details_screen, text = txt_book_details, font = ("Helvetica", 38, "bold"), foreground = "black").place(x=180, y = 20)
    
    Label(book_details_screen, text = txt_book_name, font = ("Helvetica", 21, "bold")).place(x=69, y=205)
    Label(book_details_screen, text = txt_author, font = ("Helvetica", 15), foreground = "blue").place(x=69, y=274)
    Label(book_details_screen, image = fourstar_icon).place(x=63, y=343)
    Label(book_details_screen, text = txt_marks, font = ("Helvetica", 15)).place(x=246, y=352)
    Label(book_details_screen, text = txt_summary, font = ("Helvetica", 15)).place(x=69, y=419)   

    Button(book_details_screen, text= txt_comment, font = ("Helvetica", 15, "bold"), foreground="black", width=20, height=1, cursor="hand2", command = comment).place(x=362,y=350)
    Button(book_details_screen, text= txt_read, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = page_not_found).place(x=121,y=629)
    Button(book_details_screen, text= txt_store, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = store_ebooks).place(x=562,y=629)
    Button(book_details_screen, text= txt_review, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = review).place(x=1003,y=629)

    book_details_screen.title(txt_book_details)
    book_details_screen.state("zoomed")
    book_details_screen.geometry(geometry_size)


def page_not_found():
    global page_not_found_screen
    page_not_found_screen = Toplevel(book_details_screen)
    page_not_found_screen.title("Error")
    Label(page_not_found_screen, text="Page not found").pack()
    Button(page_not_found_screen, text="OK", command=delete_page_not_found).pack()

def delete_page_not_found():
    page_not_found_screen.destroy()

def close_page():
    book_details_screen.destroy()