from tkinter import *

def labelfun ():
    newwin = Tk()
    newwin.title("Example of Button")
    newwin.configure(background="#453421")
    name_in_newwin = Label (newwin, text = "This an example of a Label created by Tkinter in Python.")
    name_in_newwin["fg"] = "white"
    name_in_newwin["bg"] = "#453421"
    name_in_newwin["padx"] = "10"
    name_in_newwin["pady"] = "10"
    name_in_newwin["font"] = "CMUsans 12"
    name_in_newwin["bd"] = "1"
    name_in_newwin["relief"] = "raised"
    name_in_newwin.pack(pady = 10)

    file = open ("./files/new_label.dat", "r")

    # read file is tuple
    tuple = file.read()
    text = ''.join(tuple)

    code_in_newwin = Label (newwin, text = text)
    code_in_newwin["bg"] = "#DBDCEA"
    code_in_newwin["fg"] = "black"
    code_in_newwin["pady"] = "10"
    code_in_newwin["padx"] = "10"
    code_in_newwin["justify"] = "left"
    code_in_newwin.pack(pady = 20, padx = 20)
