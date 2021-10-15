from tkinter import *
from PIL import Image, ImageTk
from db_conn import readFromDb, insertUpdateDeleteToDb

def comment():
    global comment_screen
    global back_icon
    comment_screen = Toplevel()

    txt_comment = "Comments"
    txt_name = "John"
    txt_comments = "The book is very interesting. I really would like to suggest this book."
    geometry_size = "1366x768"
    back_icon = ImageTk.PhotoImage(Image.open("back.png").resize((50, 50), Image.ANTIALIAS))
    Button(comment_screen, image = back_icon, cursor="hand2", command = close_page).place(x=17,y=65)
    Label(comment_screen, text = txt_comment, font = ("Helvetica", 38, "bold"), foreground = "black").place(x=50, y=95)
    Label(comment_screen, text = txt_name, font = ("Helvetica", 20, "bold"), foreground = "black").place(x=50, y=265)
    Label(comment_screen, text = txt_comments, font = ("Helvetica", 15), foreground = "black").place(x=50, y=338)

    comment_screen.title(txt_comment)
    comment_screen.state("zoomed")
    comment_screen.geometry(geometry_size)

def close_page():
    comment_screen.destroy()