from action_adventure import action_adventure
from tkinter import *
from PIL import Image, ImageTk
from db_conn import readFromDb, insertUpdateDeleteToDb
from fantasy import fantasy
from horror import horror
from romance import romance

def bookcategories():
    global book_categories_screen
    global book_categories_icon
    global search_entry
    global action_adventure_icon
    global horror_icon
    global fantasy_icon
    global romance_icon
    book_categories_screen = Toplevel()
    book_categories_icon = ImageTk.PhotoImage(Image.open("bookcategories.png").resize((50, 50), Image.ANTIALIAS))
    action_adventure_icon = ImageTk.PhotoImage(Image.open("action_adventure.png").resize((110, 120), Image.ANTIALIAS))
    horror_icon = ImageTk.PhotoImage(Image.open("horror.png").resize((110, 120), Image.ANTIALIAS))
    fantasy_icon = ImageTk.PhotoImage(Image.open("fantasy.png").resize((110, 120), Image.ANTIALIAS))
    romance_icon = ImageTk.PhotoImage(Image.open("romance.png").resize((110, 120), Image.ANTIALIAS))

    txt_book_categories = "Book Categories"
    txt_search = "Search"
    geometry_size = "1366x768"
    txt_action_Adventure = "Action/Adventure"
    txt_horror = "Horror"
    txt_fantasy = "Fantasy"
    txt_romance = "Romance"

    search_entry = Entry(book_categories_screen, font = "Helvetica 15", textvariable = txt_search, width=50)
    search_entry.place(x=100,y=90) 
    Button(book_categories_screen, text=txt_search, font = ("Helvetica", 15, "bold"), foreground="black", width=10, height=1, cursor="hand2", command = page_not_found).place(x=700,y=80)
 
    Label(book_categories_screen, image = book_categories_icon).place(x=100, y=30)
    Label(book_categories_screen, text = txt_book_categories, font = ("Helvetica", 38, "bold"), foreground = "black").place(x=180, y = 20)

    Label(book_categories_screen, image = action_adventure_icon).place(x=272, y=237)
    Label(book_categories_screen, image = horror_icon).place(x=959, y=237)
    Label(book_categories_screen, image = fantasy_icon).place(x=272, y=482)
    Label(book_categories_screen, image = romance_icon).place(x=959, y=482)

    Button(book_categories_screen, text= txt_action_Adventure, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = action_adventure).place(x=200,y=392)
    Button(book_categories_screen, text = txt_horror, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = horror).place(x=900,y=392)
    Button(book_categories_screen, text = txt_fantasy, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = fantasy).place(x=200,y=632)
    Button(book_categories_screen, text = txt_romance, font = ("Helvetica", 15, "bold"), foreground="black", width=16, height=1, cursor="hand2", command = romance).place(x=900,y=632)
    
    book_categories_screen.title(txt_book_categories)
    book_categories_screen.state("zoomed")
    book_categories_screen.geometry(geometry_size)

def page_not_found():
    global page_not_found_screen
    page_not_found_screen = Toplevel(book_categories_screen)
    page_not_found_screen.title("Error")
    Label(page_not_found_screen, text="Page not found").pack()
    Button(page_not_found_screen, text="OK", command=delete_page_not_found).pack()

def delete_page_not_found():
    page_not_found_screen.destroy()