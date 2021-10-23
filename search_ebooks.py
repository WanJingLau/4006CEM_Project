from tkinter import *
from bookdetails import bookdetails
from db_conn import readFromDb
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from bookcategories import bookcategories

def search_ebooks():
    global search_ebooks_screen
    global search_ebooks_icon
    global back_icon
    global scroll_frame2
    search_ebooks_screen = Toplevel()
    search_ebooks_icon = ImageTk.PhotoImage(Image.open("search.png").resize((80, 80), Image.ANTIALIAS))
    back_icon = ImageTk.PhotoImage(Image.open("back.png").resize((30, 30), Image.ANTIALIAS))
    #text declaration
    txt_search_ebooks = "Search E-books"
    txt_result_ebooks = "Results:"
    geometry_size = "1366x768"
    #screen size, maximize screen
    search_ebooks_screen.title(txt_search_ebooks)
    search_ebooks_screen.state("zoomed")
    search_ebooks_screen.geometry(geometry_size)
    #back button
    Button(search_ebooks_screen, image = back_icon, cursor="hand2", command = close_page).place(x=15,y=15)
    #page title & icon
    Label(search_ebooks_screen, image = search_ebooks_icon).place(x=80, y=40)
    Label(search_ebooks_screen, text = txt_search_ebooks, font = ("Helvetica", 14, "bold")).place(x=180, y = 70)
    #display result word
    Label(search_ebooks_screen, text = txt_result_ebooks, font = ("Helvetica", 12, "bold")).place(x=80, y = 140)
    #Frame 
    scroll_frame = Frame(search_ebooks_screen, height=475, width=1200, borderwidth = 1, relief=SOLID)
    scroll_frame.place(x=80, y = 190)
    #canvas with scroll bar
    scroll_canvas = Canvas(scroll_frame, width=1200, height=475)
    scroll_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    canvas_scrollbar = ttk.Scrollbar(scroll_frame, orient = VERTICAL, command=scroll_canvas.yview)
    canvas_scrollbar.pack(side=RIGHT,fill=Y)
    scroll_canvas.configure(yscrollcommand=canvas_scrollbar.set)
    scroll_frame.bind("<Configure>", lambda e: scroll_canvas.configure(scrollregion=scroll_canvas.bbox(ALL)))
    #2nd frame
    scroll_frame2 = Frame(scroll_canvas)
    scroll_canvas.create_window((0,0), window=scroll_frame2, anchor=NW)
    #display search result
    display_search_result()

def display_search_result():
    global row_frame
    txt_view_details = "View Details"
    txt_no_result = "No result shown"
    #get book name
    search_book = get_book_result()
    if search_book != []:
        y = 0
        for name in search_book:
            row_frame = Frame(scroll_frame2, height=50, width=1165, borderwidth = 1, relief = SOLID, background = "light grey", highlightcolor="light grey")
            row_frame.grid(row=y, column=0, padx=20, pady=15)
            Label(row_frame, text = name[0], background = "light grey",font = ("Helvetica", 12, "bold")).place(x=20, y=12)
            Button(row_frame, text= txt_view_details, font = ("Helvetica", 12), width=10, height=1, cursor="hand2", command = lambda name=name: bookdetails(name[0])).place(x=1045, y=7.5)
            y += 1
    else:
        Label(scroll_frame2, text = txt_no_result, font = ("Helvetica", 12, "bold"), foreground="grey").grid(padx=500, pady=225)

def get_book_result():
    global get_book
    get_book = 
    if len(get_book.get()) == 0 or get_book.get().isspace():
            entry("The Search is Empty.")
    else:
            search1 = get_book.get()
            dbQuery = """SELECT Category, Author
                        FROM dbo.Books WITH(NOLOCK) 
                        WHERE Name = N'"""+search1+"""'
                        AND isActive = 1"""
    result = readFromDb(dbQuery)
    return result

 # Designing popup for entry empty/ login invalid password
def entry(entry):
    messagebox.showerror("Failed search", entry, parent = search_ebooks_screen)
 #back button
def close_page():
    search_ebooks_screen.destroy()