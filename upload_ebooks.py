from tkinter import *
from tkinter import ttk, filedialog, scrolledtext, messagebox
from PIL import Image, ImageTk
from db_conn import readFromDb, insertUpdateDeleteToDb

def upload_ebooks():
    global upload_ebooks_screen
    global uploadbooks_icon
    global search_combobox
    global book_name_entry
    global author_entry
    global summary_scrolledText
    global book_name
    global author
    global filename
    global bindata
    global lbl_no_file_chosen
    global txt_no_file_chosen
    #variable declaration
    upload_ebooks_screen = Toplevel()
    uploadbooks_icon = ImageTk.PhotoImage(Image.open("uploadbooks.png").resize((80, 80), Image.ANTIALIAS))
    book_name = StringVar()
    author = StringVar()
    #text variable declaration
    txt_upload_ebooks = "Upload / Add E-books"
    geometry_size = "1366x768"
    txt_book_category = "Select Book Category"
    txt_book_name = "Enter Book Name"
    txt_author = "Enter Author"
    txt_summary = "Enter Book Summary"
    txt_content = "Book Content"
    txt_file = "Upload File (.pdf)"
    txt_submit = "Submit"  
    txt_no_file_chosen = "No File Chosen"
    #screen title,size, maximize windows
    upload_ebooks_screen.title(txt_upload_ebooks)
    upload_ebooks_screen.geometry(geometry_size)
    upload_ebooks_screen.state("zoomed")
    #page title
    Label(upload_ebooks_screen, image = uploadbooks_icon).place(x=80, y=40)
    Label(upload_ebooks_screen, text = txt_upload_ebooks, font = ("Helvetica", 14, "bold"), foreground = "black").place(x=180, y = 70)
    #book_name
    Label(upload_ebooks_screen, text = txt_book_name, font = ("Helvetica", 12, "bold"), foreground = "blue").place(x=80,y=130)
    book_name_entry = Entry(upload_ebooks_screen, textvariable = book_name, font = "Helvetica 12", width=50)
    book_name_entry.place(x=80,y=160)
    book_name_entry.focus_set()
    #author
    Label(upload_ebooks_screen, text = txt_author, font = ("Helvetica", 12, "bold"), foreground = "blue").place(x=580,y=130)
    author_entry = Entry(upload_ebooks_screen, textvariable = author, font = "Helvetica 12", width=50)
    author_entry.place(x=580,y=160)
    #book category
    Label(upload_ebooks_screen, text = txt_book_category, font = ("Helvetica", 12, "bold"), foreground = "blue").place(x=80,y=200)
    search_combobox = ttk.Combobox(upload_ebooks_screen, values=("Action/Adventure", "Horror","Fantasy","Romance"), state = "readonly") 
    search_combobox.place(x=80,y=230)
    #upload file
    Label(upload_ebooks_screen, text = txt_content, font = ("Helvetica", 12, "bold"), foreground = "blue").place(x=580,y=200)
    Button(upload_ebooks_screen, text= txt_file, font = ("Helvetica", 12, "bold"), foreground="black", background="light grey", width=16, cursor="hand2", command = UploadAction).place(x=580,y=230)   
    lbl_no_file_chosen = Label(upload_ebooks_screen, text = txt_no_file_chosen, font = ("Helvetica", 12))
    lbl_no_file_chosen.place(x=760,y=235)
    #summary
    Label(upload_ebooks_screen, text = txt_summary, font = ("Helvetica", 12, "bold"), foreground = "blue").place(x=80,y=270)
    summary_scrolledText = scrolledtext.ScrolledText(upload_ebooks_screen, font = ("Helvetica", 12), width=105, height=10)
    summary_scrolledText.place(x=80,y=300)
    #Submit button
    Button(upload_ebooks_screen, text= txt_submit, font = ("Helvetica", 12, "bold"), foreground="white", background="blue", width=20, height=1, cursor="hand2", command = book_verify).place(x=590,y=550)

def UploadAction():
    filename = filedialog.askopenfilename(parent = upload_ebooks_screen, initialdir = "/", title = "Select file", filetypes = [("PDF files","*.pdf")])
    if filename:
        lbl_no_file_chosen.config(text = filename) #change no file chosen text to file path
        with open(filename, 'rb') as f:
            bindata = f.read()

def book_verify():
    if len(book_name.get()) == 0:
        entry("Book Name is empty. Please enter Book Name.")
    elif len(author.get()) == 0:
        entry("Book Author is empty. Please enter Author.")
    elif len(search_combobox.get()) == 0:
        entry("No Book Category is selected. Please select Book Category.")
    elif lbl_no_file_chosen.cget("text") == txt_no_file_chosen:
        entry(txt_no_file_chosen + ". Please select a PDF file to upload.")
    elif len(summary_scrolledText.get()) == 0:
        entry("Book Summary is empty. Please enter Book Summary.")

def entry(entry):
   messagebox.showerror("Failed Upload", entry, parent = upload_ebooks_screen)
