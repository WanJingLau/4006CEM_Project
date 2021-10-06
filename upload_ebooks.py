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
    txt_book_category = "Select Book Category"
    txt_select = "Select Type"
    txt_book_name = "Enter Book Name"
    txt_author = "Enter Author"
    txt_summary = "Enter Summary of book"
    txt_content = "Content of book"
    txt_file = "Insert pdf file"
    txt_submit = "Submit"  

    Label(upload_ebooks_screen, image = uploadbooks_icon).place(x=100, y=30)
    Label(upload_ebooks_screen, text = txt_upload_ebooks, font = ("Helvetica", 38, "bold"), foreground = "black").place(x=180, y = 20)

    Label(upload_ebooks_screen, text = txt_book_category, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=50,y=130)
    search_entry = Entry(upload_ebooks_screen, font = "Helvetica 15", textvariable = txt_select, width=50)
    search_entry.place(x=327,y=130)
    Button(upload_ebooks_screen, text=txt_select, font = ("Helvetica", 15, "bold"), foreground="black", width=10, height=1, cursor="hand2", command = page_not_found).place(x=900,y=120) 

    Label(upload_ebooks_screen, text = txt_book_name, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=50,y=180)
    old_username_entry = Entry(upload_ebooks_screen, font = "Helvetica 12", width=50)
    old_username_entry.place(x=50,y=220)
    Label(upload_ebooks_screen, text = txt_author, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=50,y=295)
    new_username_entry = Entry(upload_ebooks_screen, font = "Helvetica 12", width=50)
    new_username_entry.place(x=50,y=340)
    Label(upload_ebooks_screen, text = txt_summary, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=50,y=403)
    confirm_username_entry = Entry(upload_ebooks_screen, font = "Helvetica 12", width=50)
    confirm_username_entry.place(x=50,y=440)
    Label(upload_ebooks_screen, text = txt_content, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=50,y=503)
    Button(upload_ebooks_screen, text= txt_file, font = ("Helvetica", 15, "bold"), foreground="black", background="light grey", width=16, height=1, cursor="hand2", command = page_not_found).place(x=50,y=558)

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