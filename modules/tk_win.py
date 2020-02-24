from tkinter import *

def winfun ():
    newwin = Tk()
    newwin.title("Example of Window")
    newwin.configure(background="white")
    name_in_newwin = Label (newwin, text = "This an example of a window created by Tkinter in Python.")
    name_in_newwin["bg"] = "white"
    name_in_newwin["fg"] = "black"
    name_in_newwin["font"] = "CMUsans 12"
    name_in_newwin.pack()

    file = open ("./files/new_win.dat", "r")

    # read file is tuple
    tuple = file.read()
    text = ''.join(tuple)

    code_in_newwin = Label (newwin, text = text)
    code_in_newwin["bg"] = "#DBDAEA"
    code_in_newwin["fg"] = "black"
    code_in_newwin["font"] = "Helvetica 8"
    code_in_newwin["pady"] = "10"
    code_in_newwin["justify"] = "left"
    code_in_newwin.pack()
