from tkinter import *
from db_conn import readFromDb
import guli

def download_ebooks():
    ebook = guli.GuliVariable("download_book").get()
    dbQuery = """SELECT BookContent 
                FROM dbo.Books WITH(NOLOCK)
                WHERE Name = N'"""+ebook+"""'"""
    result = readFromDb(dbQuery)
