from tkinter import *
from PIL import Image, ImageTk
from db_conn import readFromDb, insertUpdateDeleteToDb

def bookcategories():
    global book_categories_screen
    global left_icon
    global right_icon
    global book_categories_icon
    global search_entry
    global Book1_icon
    global Book2_icon
    global Book3_icon
    global Book4_icon
    global Book5_icon
    global Book6_icon
    global Book7_icon
    global Book8_icon
    global action_Adventure
    global horror
    global fantasy
    global romance
    book_categories_screen = Toplevel()
    book_categories_icon = ImageTk.PhotoImage(Image.open("bookcategories.png").resize((50, 50), Image.ANTIALIAS))
    left_icon = ImageTk.PhotoImage(Image.open("left.png").resize((50, 50), Image.ANTIALIAS))
    right_icon = ImageTk.PhotoImage(Image.open("right.png").resize((50, 50), Image.ANTIALIAS))
    Book1_icon = ImageTk.PhotoImage(Image.open("Book1.png").resize((180, 220), Image.ANTIALIAS))
    Book2_icon = ImageTk.PhotoImage(Image.open("Book2.png").resize((180, 220), Image.ANTIALIAS))
    Book3_icon = ImageTk.PhotoImage(Image.open("Book3.png").resize((180, 220), Image.ANTIALIAS))
    Book4_icon = ImageTk.PhotoImage(Image.open("Book4.png").resize((180, 220), Image.ANTIALIAS))
    Book5_icon = ImageTk.PhotoImage(Image.open("Book5.png").resize((180, 220), Image.ANTIALIAS))
    Book6_icon = ImageTk.PhotoImage(Image.open("Book6.png").resize((180, 220), Image.ANTIALIAS))
    Book7_icon = ImageTk.PhotoImage(Image.open("Book7.png").resize((180, 220), Image.ANTIALIAS))
    Book8_icon = ImageTk.PhotoImage(Image.open("Book8.png").resize((180, 220), Image.ANTIALIAS))

    txt_book_categories = "Book Categories"
    txt_search = "Search"
    geometry_size = "1366x768"
    txt_read = "Read"
    txt_action_Adventure = "Action/Adventure"
    txt_horror = "Horror"
    txt_fantasy = "Fantasy"
    txt_romance = "Romance"

    search_entry = Entry(book_categories_screen, font = "Helvetica 15", textvariable = txt_search, width=50)
    search_entry.place(x=100,y=90) 
    Button(book_categories_screen, text=txt_search, font = ("Helvetica", 15, "bold"), foreground="black", width=10, height=1, cursor="hand2", command = page_not_found).place(x=700,y=80)
 
    Label(book_categories_screen, image = book_categories_icon).place(x=100, y=30)
    Label(book_categories_screen, text = txt_book_categories, font = ("Helvetica", 38, "bold"), foreground = "black").place(x=180, y = 20)
    
    Label(book_categories_screen, image = Book1_icon).place(x=184, y=185)
    Button(book_categories_screen, text= txt_action_Adventure, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = page_not_found).place(x=44,y=138)
    Button(book_categories_screen, text= txt_read, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = page_not_found).place(x=191,y=388)
    
    Label(book_categories_screen, image = Book2_icon).place(x=378, y=188)
    Button(book_categories_screen, text = txt_read, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = page_not_found).place(x=378,y=388)
   
    Label(book_categories_screen, image = Book3_icon).place(x=893, y=174)
    Button(book_categories_screen, text = txt_horror, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = page_not_found).place(x=700,y=130)
    Button(book_categories_screen, text = txt_read, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = page_not_found).place(x=893,y=388)
    
    Label(book_categories_screen, image = Book4_icon).place(x=1071, y=185)
    Button(book_categories_screen, text = txt_read, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = page_not_found).place(x=1071,y=388)
    
    Label(book_categories_screen, image = Book5_icon).place(x=186, y=496)
    Button(book_categories_screen, text = txt_fantasy, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = page_not_found).place(x=29,y=446)
    Button(book_categories_screen, text = txt_read, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = page_not_found).place(x=186,y=704)
    
    Label(book_categories_screen, image = Book6_icon).place(x=372, y=496)
    Button(book_categories_screen, text = txt_read, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = page_not_found).place(x=372,y=704)
    
    Label(book_categories_screen, image = Book7_icon).place(x=893, y=485)
    Button(book_categories_screen, text = txt_romance, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = page_not_found).place(x=700,y=446)
    Button(book_categories_screen, text = txt_read, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = page_not_found).place(x=898,y=704)

    Label(book_categories_screen, image = Book8_icon).place(x=1071, y=485)
    Button(book_categories_screen, text = txt_read, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = page_not_found).place(x=1081,y=704)

    book_categories_screen.title(txt_book_categories)
    book_categories_screen.geometry(geometry_size)


def page_not_found():
    global page_not_found_screen
    page_not_found_screen = Toplevel(book_categories_screen)
    page_not_found_screen.title("Error")
    Label(page_not_found_screen, text="Page not found").pack()
    Button(page_not_found_screen, text="OK", command=delete_page_not_found).pack()

def delete_page_not_found():
    page_not_found_screen.destroy()