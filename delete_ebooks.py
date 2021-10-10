from tkinter import *
from PIL import Image, ImageTk
from db_conn import readFromDb, insertUpdateDeleteToDb

def delete_ebooks():
    global delete_ebooks_screen
    global deleteebooks_icon
    delete_ebooks_screen = Toplevel()
    deleteebooks_icon = ImageTk.PhotoImage(Image.open("deleteebooks.png").resize((50, 50), Image.ANTIALIAS))

    txt_delete_ebooks = "Delete E-Books"
    txt_select = "Select"
    txt_delete = "Delete"
    geometry_size = "1366x768"
    txt_book_name = "Book Name:"   

    Label(delete_ebooks_screen, image = deleteebooks_icon).place(x=100, y=30)
    Label(delete_ebooks_screen, text = txt_delete_ebooks, font = ("Helvetica", 38, "bold"), foreground = "black").place(x=180, y = 20)

    search_entry = Entry(delete_ebooks_screen, font = "Helvetica 15", textvariable = txt_select, width=70)
    search_entry.place(x=110,y=110)
    Button(delete_ebooks_screen, text=txt_select, font = ("Helvetica", 15, "bold"), foreground="black", width=10, height=1, cursor="hand2", command = page_not_found).place(x=900,y=100) 

    Label(delete_ebooks_screen, text = txt_book_name, font = ("Helvetica", 15, "bold"), foreground = "blue").place(x=50,y=200)
    old_username_entry = Entry(delete_ebooks_screen, font = "Helvetica 12", width=90)
    old_username_entry.place(x=50,y=250)

    Button(delete_ebooks_screen, text= txt_delete, font = ("Helvetica", 15, "bold"), foreground="white", background="blue", width=16, height=1, cursor="hand2", command = page_not_found).place(x=1101,y=669)

    delete_ebooks_screen.title(txt_delete_ebooks)
    delete_ebooks_screen.state("zoomed")
    delete_ebooks_screen.geometry(geometry_size)

def page_not_found():
    global page_not_found_screen
    page_not_found_screen = Toplevel(delete_ebooks_screen)
    page_not_found_screen.title("Error")
    Label(page_not_found_screen, text="Page not found").pack()
    Button(page_not_found_screen, text="OK", command=delete_page_not_found).pack()

def delete_page_not_found():
    page_not_found_screen.destroy()