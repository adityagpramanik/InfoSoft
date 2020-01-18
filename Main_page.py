from tkinter import *
from tkinter import messagebox

def winfun ():
    newwin = Tk()
    newwin.title("Example of Window")
    newwin.configure(background="white")
    name_in_newwin = Label (newwin, text = "This an example of a window created by Tkinter in Python.")
    name_in_newwin["bg"] = "white"
    name_in_newwin["fg"] = "black"
    name_in_newwin["font"] = "CMUsans 12"
    name_in_newwin.pack()

    file = open ("new_win.dat", "r")

    # read file is tuple
    tuple = file.read()
    text = ' '.join(tuple)

    code_in_newwin = Label (newwin, text = text)
    code_in_newwin["bg"] = "#DBDAEA"
    code_in_newwin["fg"] = "black"
    code_in_newwin["font"] = "Helvetica 8"
    code_in_newwin["pady"] = "10"
    code_in_newwin["justify"] = "left"
    code_in_newwin.pack()

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

    file = open ("new_frame.dat", "r")

    # read file is tuple
    tuple = file.read()
    text = ' '.join(tuple)

    code_in_newwin = Label (newwin, text = text)
    code_in_newwin["bg"] = "#DBDCEA"
    code_in_newwin["fg"] = "black"
    code_in_newwin["pady"] = "10"
    code_in_newwin["padx"] = "10"
    code_in_newwin["justify"] = "left"
    code_in_newwin.pack(pady = 20, padx = 20)

def Butfun ():
    newwin = Tk()
    newwin.title("Example of Button")
    newwin.configure(background="#453421")
    name_in_newwin = Label (newwin, text = "This an example of a Button created by Tkinter in Python.")
    name_in_newwin["fg"] = "white"
    name_in_newwin["bg"] = "#453421"
    name_in_newwin["font"] = "CMUsans 12"
    name_in_newwin.pack(pady = 5, padx = 5)

    click_but = Button(newwin, text = "Click Me", fg = "black", command = clickme)
    click_but.pack()

    file = open ("new_frame.dat", "r")

    # read file is tuple
    tuple = file.read()
    text = ' '.join(tuple)

    code_in_newwin = Label (newwin, text = text)
    code_in_newwin["bg"] = "#DBDCEA"
    code_in_newwin["fg"] = "black"
    code_in_newwin["pady"] = "10"
    code_in_newwin["padx"] = "10"
    code_in_newwin["justify"] = "left"
    code_in_newwin.pack(pady = 20, padx = 20)

def clickme ():
    print("Hey There")

def new_exit ():
    MsgBox = messagebox.askquestion ("Exiting", "Are you sure to want to exit?", icon = "warning")
    if MsgBox == "yes":
        exit()

# window creation
def main ():
    win = Tk()

    win.title("InfoSoft")
    win.configure(background="#857E61")

    # create label
    main_label = Label (win, text = "InfoSoft", bg = "#383838", fg = "white", font = "CMUsans 18 bold")
    main_label.pack(fill = "x")

    second_label = Label (win, text = "A Python based software to know the use of TKinter GUI library.", bg = "#383838", fg = "white", font = "CMUsans 12 bold")
    second_label.pack(fill = "x")

    topframe = Frame(win, background = "#857E61")
    topframe.pack(pady = "20", expand = 0)

    bottomframe = Frame(win)
    bottomframe.pack(pady = "20", side = "bottom")

    b1 = Button (topframe, text = "Window ", fg = "black", command = winfun, relief = "raised", bd = "3" )
    b2 = Button (topframe, text = "Frame", fg = "black", command = framefun, relief = "raised", bd = "3")
    b3 = Button (topframe, text = "Button", fg = "black", command = clickme )
    b4 = Button (topframe, text = "Button3", fg = "black", command = clickme )
    b5 = Button (topframe, text = "Button4", fg = "black", command = clickme )
    exit_button = Button (bottomframe, text = "Exit", fg = "black", command = new_exit)

    b1.pack(padx = "10", pady = "10", side = "left")
    b2.pack(padx = "10", pady = "10", side = "left")
    b3.pack(padx = "10", pady = "10", side = "left")
    b4.pack(padx = "10", pady = "10", side = "left")
    b5.pack(padx = "10", pady = "10", side = "left")
    exit_button.pack()

    win.mainloop()
if __name__ == "__main__":
    main()
