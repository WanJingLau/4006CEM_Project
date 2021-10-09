from tkinter import *
from PIL import Image, ImageTk
from db_conn import readFromDb, insertUpdateDeleteToDb

def review():
    global review_screen
    global starrate_icon
    review_screen = Toplevel()
    starrate_icon = ImageTk.PhotoImage(Image.open("starrate.png").resize((160, 70), Image.ANTIALIAS))

    txt_review = "Review"
    geometry_size = "1366x768"
    txt_comments = "Comments:"
    txt_rating = "Rating (Please select a star amount):"
    txt_submit = "Submit"
    txt_amount = " 1   2  3   4   5"

    Label(review_screen, image = starrate_icon).place(x=420, y=535)
    Label(review_screen, text = txt_review, font = ("Helvetica", 38, "bold"), foreground = "black").place(x=50, y=95)
    Label(review_screen, text = txt_amount, font = ("Helvetica", 15, "bold"), foreground = "black").place(x=430, y=619)
    Button(review_screen, text= txt_submit, font = ("Helvetica", 15, "bold"), foreground="white", background="blue", width=16, height=1, cursor="hand2", command = page_not_found).place(x=1101,y=669)
    Label(review_screen, text = txt_rating, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=60, y=468)

    Label(review_screen, text = txt_comments, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=60, y=218)

    review_screen.title(txt_review)
    review_screen.state("zoomed")
    review_screen.geometry(geometry_size)

def page_not_found():
    global page_not_found_screen
    page_not_found_screen = Toplevel(review_screen)
    page_not_found_screen.title("Error")
    Label(page_not_found_screen, text="Page not found").pack()
    Button(page_not_found_screen, text="OK", command=delete_page_not_found).pack()

def delete_page_not_found():
    page_not_found_screen.destroy()