from tkinter import *
from db_conn import readFromDb
import guli

def read_ebooks():
    global read_ebooks_screen
    read_ebooks_screen = Toplevel()
    
def get_book_content():
    ebook = guli.GuliVariable("read_book").get()
    dbQuery = """SELECT BookContent 
                FROM dbo.Books WITH(NOLOCK)
                WHERE Name = N'"""+ebook+"""'"""
    result = readFromDb(dbQuery)