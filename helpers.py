#check & replace to 2 single quote
from tkinter import mainloop
from typing import Mapping


def check_single_quote(string):
    if string.find("'") != -1:
        return string.replace("'", "''")
    else:
        return string
#check & replace spacing with _
def check_spacing(string):
    if string.find(" ") != -1:
        return string.replace(" ", "_")
    else:
        return string
#check & remove ?
def check_question_mark(string):
    if string.find("?") != -1:
        return string.replace("?", "")
    else:
        return string

def home():
    for widget in root.mainloop:
        if isinstance(widget, tk.Toplevel):
            widget.destroy()