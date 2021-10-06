from tkinter import *
from PIL import Image, ImageTk
from db_conn import readFromDb, insertUpdateDeleteToDb

def upload_ebooks():
    global upload_ebooks_screen
    global uploadbooks_icon
    global search_entry
    upload_ebooks_screen = Toplevel()
    uploadbooks_icon = ImageTk.PhotoImage(Image.open("uploadbooks.png").resize((50, 50), Image.ANTIALIAS))

    txt_upload_ebooks = "Upload / Add E-books"
    geometry_size = "1366x768"
    txt_book_name = "Enter Book Name"
    txt_author = "Enter Author"
    txt_summary = "Enter Summary of book"
    txt_content = "Content of book"
    txt_submit = "Submit"  

    Label(upload_ebooks_screen, image = uploadbooks_icon).place(x=100, y=30)
    Label(upload_ebooks_screen, text = txt_upload_ebooks, font = ("Helvetica", 38, "bold"), foreground = "black").place(x=180, y = 20)

    Frame(upload_ebooks_screen, background="white", width=684, height=55).place(x=30, y=211)
    Frame(upload_ebooks_screen, background="white", width=684, height=55).place(x=30, y=292)
    Frame(upload_ebooks_screen, background="white", width=684, height=91).place(x=30, y=373)
    Frame(upload_ebooks_screen, background="white", width=684, height=149).place(x=30, y=490)
    Label(upload_ebooks_screen, text = txt_book_name, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=263, y=219)
    Label(upload_ebooks_screen, text = txt_author, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=300, y=300)
    Label(upload_ebooks_screen, text = txt_summary, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=209, y=399)
    Label(upload_ebooks_screen, text = txt_content, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=277, y=545)
    Button(upload_ebooks_screen, text= txt_submit, font = ("Helvetica", 15, "bold"), foreground="white", background="blue", width=16, height=1, cursor="hand2", command = page_not_found).place(x=1101,y=669)

    upload_ebooks_screen.title(txt_upload_ebooks)
    upload_ebooks_screen.geometry(geometry_size)

def page_not_found():
    global page_not_found_screen
    page_not_found_screen = Toplevel(upload_ebooks_screen)
    page_not_found_screen.title("Error")
    Label(page_not_found_screen, text="Page not found").pack()
    Button(page_not_found_screen, text="OK", command=delete_page_not_found).pack()

def delete_page_not_found():
    page_not_found_screen.destroy()   