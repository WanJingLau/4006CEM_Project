from tkinter import *
from PIL import Image, ImageTk
from db_conn import readFromDb, insertUpdateDeleteToDb

def edit_ebooks():
    global edit_ebooks_screen
    global editebooks_icon
    global back_icon
    edit_ebooks_screen = Toplevel()
    editebooks_icon = ImageTk.PhotoImage(Image.open("editebooks.png").resize((50, 50), Image.ANTIALIAS))

    txt_edit_ebooks = "Edit E-Books"
    txt_select = "Select"
    geometry_size = "1366x768"
    txt_update_book_details = "Update Book Details"
    txt_book_name = "Book Name:"
    txt_author = "Author:"
    txt_summary = "Summary of Book:"
    txt_content = "New Content:"
    txt_insert = "Insert new pdf file"
    txt_submit = "Submit"
    back_icon = ImageTk.PhotoImage(Image.open("back.png").resize((50, 50), Image.ANTIALIAS))
    Button(edit_ebooks_screen, image = back_icon, cursor="hand2", command = close_page).place(x=17,y=65)

    Label(edit_ebooks_screen, image = editebooks_icon).place(x=100, y=30)
    Label(edit_ebooks_screen, text = txt_edit_ebooks, font = ("Helvetica", 38, "bold"), foreground = "black").place(x=180, y = 20)

    search_entry = Entry(edit_ebooks_screen, font = "Helvetica 15", textvariable = txt_select, width=70)
    search_entry.place(x=100,y=90)
    Button(edit_ebooks_screen, text=txt_select, font = ("Helvetica", 15, "bold"), foreground="black", width=10, height=1, cursor="hand2", command = page_not_found).place(x=900,y=80) 

    Label(edit_ebooks_screen, text = txt_update_book_details, font = ("Helvetica", 15, "bold"), foreground = "black").place(x=50, y = 150)
    
    Label(edit_ebooks_screen, text = txt_book_name, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=50,y=200)
    old_username_entry = Entry(edit_ebooks_screen, font = "Helvetica 12", width=50)
    old_username_entry.place(x=50,y=250)
    Label(edit_ebooks_screen, text = txt_author, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=50,y=300)
    new_username_entry = Entry(edit_ebooks_screen, font = "Helvetica 12", width=50)
    new_username_entry.place(x=50,y=350)
    Label(edit_ebooks_screen, text = txt_summary, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=50,y=400)
    confirm_username_entry = Entry(edit_ebooks_screen, font = "Helvetica 12", width=50)
    confirm_username_entry.place(x=50,y=450)
    Label(edit_ebooks_screen, text = txt_content, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=50,y=503)
    Button(edit_ebooks_screen, text= txt_insert, font = ("Helvetica", 15, "bold"), foreground="black", background="light grey", width=16, height=1, cursor="hand2", command = page_not_found).place(x=50,y=555)

    Button(edit_ebooks_screen, text= txt_submit, font = ("Helvetica", 15, "bold"), foreground="white", background="blue", width=16, height=1, cursor="hand2", command = page_not_found).place(x=1101,y=669)

    edit_ebooks_screen.title(txt_edit_ebooks)
    edit_ebooks_screen.state("zoomed")
    edit_ebooks_screen.geometry(geometry_size)

def page_not_found():
    global page_not_found_screen
    page_not_found_screen = Toplevel(edit_ebooks_screen)
    page_not_found_screen.title("Error")
    Label(page_not_found_screen, text="Page not found").pack()
    Button(page_not_found_screen, text="OK", command=delete_page_not_found).pack()

def delete_page_not_found():
    page_not_found_screen.destroy()

def close_page():
    edit_ebooks_screen.destroy()