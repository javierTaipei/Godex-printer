from tkinter import *
from tkinter import ttk
import win32api
import win32print
import tempfile

def INFO():
    printText = text.get("1.0", END)
    print(printText)
    print(printerdef)
    filename = tempfile.mktemp(".txt")
    open(filename, "w").write(printText)    
    win32api.ShellExecute(
        0,
        "printto",
        filename,
        '"%s"' % win32print.GetDefaultPrinter(),
        ".",
        0
    )
