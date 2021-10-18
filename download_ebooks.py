from tkinter import *
from tkinter import ttk, filedialog, messagebox
from db_conn import readFromDb
from reportlab.pdfgen import canvas
import guli

def download_ebooks():
    global download_ebooks_screen
    global progress_bar
    download_ebooks_screen = Toplevel()
    #text declaration
    txt_download_ebooks = "Download E-books"
    geometry_size = "1366x768"
    #screen title, screen size, maximize window
    download_ebooks_screen.title(txt_download_ebooks)
    download_ebooks_screen.state("zoomed")
    download_ebooks_screen.geometry(geometry_size)
    #progress bar
    progress_bar = ttk.Progressbar(download_ebooks_screen, orient = HORIZONTAL, length = 100, mode = "indeterminate")
    progress_bar.pack(expand=1)
    #get_pdf()

def download_action():
    global filename
    filename = filedialog.asksaveasfilename(parent = download_ebooks_screen, initialdir = "/", title = "Save As", defaultextension = ".pdf", filetypes = [("PDF files","*.pdf")])
    if filename:
        download_pdf()
    else:
        close_page()

def get_pdf():
    global result
    ebook = guli.GuliVariable("download_book").get()
    dbQuery = """SELECT BookContent 
                FROM dbo.Books WITH(NOLOCK)
                WHERE Name = N'"""+ebook+"""'"""
    result = readFromDb(dbQuery)
    if result != []:
        download_action()
    else:
        messagebox.showinfo("Failed Download","No PDF file available. Please try again later.", parent = download_ebooks_screen)
        close_page()

def download_pdf():
    canvas.Canvas(filename)
    with open(filename, 'wb') as f:
        f.write(result)
        f.close()

def close_page():
    download_ebooks_screen.destroy()
