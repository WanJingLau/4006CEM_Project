from tkinter.font import BOLD
from helpers import check_single_quote
import guli
from comment import comment
from review_ebooks import review_ebooks
from read_ebooks import read_ebooks
from tkinter import *
from tkinter import scrolledtext, messagebox
from PIL import Image, ImageTk
from db_conn import readFromDb
from threading import Thread

def bookdetails():
    global book_details_screen
    global book_categories_icon
    global book_details_image
    global back_icon
    global lbl_book_author
    global lbl_book_rating
    global summary_scrolledText
    book_details_screen = Toplevel()
    book_categories_icon = ImageTk.PhotoImage(Image.open("bookcategories.png").resize((80, 80), Image.ANTIALIAS))
    book_details_image = ImageTk.PhotoImage(Image.open("book_details_image.png").resize((330, 210), Image.ANTIALIAS))
    back_icon = ImageTk.PhotoImage(Image.open("back.png").resize((30, 30), Image.ANTIALIAS))
    #text declaration
    txt_book_details = "Book Details"
    geometry_size = "1366x768"
    txt_read = "Read"
    txt_store = "Store"
    txt_review = "Review"
    txt_comment = "View Comment"
    txt_book_name = "Book Name:"
    txt_author = "Author:"
    txt_rating = "Ratings:"
    txt_summary = "Summary:"
    #screen title, size, maximize windows
    book_details_screen.title(txt_book_details)
    book_details_screen.state("zoomed")
    book_details_screen.geometry(geometry_size)
    #back button
    Button(book_details_screen, image = back_icon, cursor="hand2", command = close_page).place(x=15,y=15)
    #page title, icon
    Label(book_details_screen, image = book_categories_icon).place(x=80, y=40)
    Label(book_details_screen, image = book_details_image).place(x=1010, y=80)
    Label(book_details_screen, text = txt_book_details, font = ("Helvetica", 14, BOLD)).place(x=180, y = 70)
    #book name
    Label(book_details_screen, text = txt_book_name, font = ("Helvetica", 12, BOLD)).place(x=80, y=140)
    Label(book_details_screen, text = guli.GuliVariable("book_name").get(), font = ("Helvetica", 12, BOLD)).place(x=180, y =140)
    #author
    Label(book_details_screen, text = txt_author, font = ("Helvetica", 12,BOLD)).place(x=80, y=180)
    lbl_book_author = Label(book_details_screen, font = ("Helvetica", 12, BOLD))
    lbl_book_author.place(x=180, y =180)
    #rating
    Label(book_details_screen, text = txt_rating, font = ("Helvetica", 12, BOLD)).place(x=80, y=220)
    lbl_book_rating = Label(book_details_screen, font = ("Helvetica", 12, BOLD))
    lbl_book_rating.place(x=180, y =220)
    #summary
    Label(book_details_screen, text = txt_summary, font = ("Helvetica", 12, BOLD)).place(x=80, y=260)
    summary_scrolledText = scrolledtext.ScrolledText(book_details_screen, state = DISABLED, font = ("Helvetica", 12), width=105, height=10)
    summary_scrolledText.place(x=80,y=290)  
    #read button
    Button(book_details_screen, text= txt_read, font = ("Helvetica", 12, BOLD), width=16, height=2, cursor="hand2", command = read_book).place(x=80,y=580)
    #store button
    Button(book_details_screen, text= txt_store, font = ("Helvetica", 12, BOLD), width=16, height=2, cursor="hand2", command = close_page).place(x=420,y=580)
    #review button
    Button(book_details_screen, text= txt_review, font = ("Helvetica", 12, BOLD), width=16, height=2, cursor="hand2", command = review_book).place(x=760,y=580)
    #view comment button
    Button(book_details_screen, text= txt_comment, font = ("Helvetica", 12, BOLD), width=16, height=2, cursor="hand2", command = close_page).place(x=1100,y=580)
    
    Thread(target= get_book_details).start()

def close_page():
    book_details_screen.destroy()

def read_book():
    guli.GuliVariable("read_book").setValue(guli.GuliVariable("book_name").get())
    read_ebooks()

def review_book():
    book_name = check_single_quote(guli.GuliVariable("book_name").get())
    email_address = guli.GuliVariable("email_add").get()
    dbQuery = """SELECT 1 
                 FROM dbo.UserBookRating WITH(NOLOCK)
                 WHERE UserId = (
                                    SELECT Id FROM dbo.Users WITH(NOLOCK) WHERE email = N'"""+email_address+"""'
                                )
                 AND BookId = (
                                    SELECT Id FROM dbo.Books WITH(NOLOCK) WHERE Name = N'"""+book_name+"""' AND isActive = 1
                              )"""
    result = readFromDb(dbQuery)
    if result == None:
        guli.GuliVariable("review_book").setValue(guli.GuliVariable("book_name").get())
        review_ebooks()
    else:
        messagebox.showinfo("Review Failed", "You have reviewed this book before. Please select another book. Thanks.", parent = book_details_screen)

def get_book_details():
    book_name = check_single_quote(guli.GuliVariable("book_name").get())
    dbQuery = """SELECT B.Author, B.Summary, UBR.Rating
                 FROM dbo.Books B WITH(NOLOCK)
                 OUTER APPLY(
                                SELECT CASE 
                                        WHEN CONVERT(DECIMAL(18,1),SUM(Rating)*1.0/Count(Rating)) IS NULL THEN 0.0 
										ELSE CONVERT(DECIMAL(18,1),SUM(Rating)*1.0/Count(Rating)) 
                                       END AS Rating
                                FROM dbo.UserBookRating WITH(NOLOCK)
                                WHERE BookId = B.Id
                            )UBR
                 WHERE B.Name = N'"""+book_name+"""'
                 AND B.isActive = 1"""
    result = readFromDb(dbQuery)
    if result != None:
        lbl_book_author.config(text=result[0])
        summary_scrolledText.config(state=NORMAL)
        summary_scrolledText.insert(INSERT, result[1])
        summary_scrolledText.config(state=DISABLED)
        lbl_book_rating.config(text=result[2])