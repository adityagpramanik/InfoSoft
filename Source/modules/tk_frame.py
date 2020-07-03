from tkinter import *

def framefun ():
    newwin = Tk()
    newwin.title("Example of Frame")
    newwin.configure(background="#453421")
    name_in_newwin = Label (newwin, text = "This an example of a frame created by Tkinter in Python.")
    name_in_newwin["fg"] = "white"
    name_in_newwin["bg"] = "#453421"
    name_in_newwin["font"] = "CMUsans 12"
    name_in_newwin.pack(pady = 5, padx = 5)

    tframe = Frame(newwin, background = "#857E61")
    tflabel = Label(tframe, text = "Top Frame")
    bframe = Frame(newwin, background = "#607A61")
    bflabel = Label(bframe, text = "Bottom Frame")
    rframe = Frame(newwin, background = "#457E61")
    rflabel = Label(rframe, text = "Right Frame")
    lframe = Frame(newwin, background = "#157E61")
    lflabel = Label(lframe, text = "Left Frame")

    tframe.pack(side = "top",fill = "x",pady = "10", padx = "10")
    bframe.pack(side = "bottom", fill = "x", pady = "10", padx = "10")
    rframe.pack(side = "right", fill = "y", pady = "10", padx = "10")
    lframe.pack(side = "left", fill = "y", pady = "10", padx = "10")
    tflabel.pack(pady = 5, padx = 5)
    bflabel.pack(pady = 5, padx = 5)
    rflabel.pack(pady = 5, padx = 5)
    lflabel.pack(pady = 5, padx = 5)

    file = open ("./files/new_frame.dat", "r")

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
