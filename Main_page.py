from tkinter import *
def winfun ():
    newwin = Tk()
    newwin.title("Window")
    newwin.configure(background="white")

def clickme ():
    print("Hey There")
# window creation
def main ():
    win = Tk()

    win.title("Happy Coding")
    win.configure(background="white")

    # create label
    main_label = Label (win, text = "InfoSoft", bg = "#383838", fg = "white", font = "CMUsans 18 bold")
    main_label.pack(fill = "x")

    second_label = Label (win, text = "A Python based software to know the use of TKinter GUI library.", bg = "#383838", fg = "white", font = "CMUsans 12 bold")
    second_label.pack(fill = "x")

    topframe = Frame(win)
    topframe.pack(side = "top")

    b1 = Button (topframe, text = "Window ", fg = "black", command = clickme )
    b2 = Button (topframe, text = "Button2", fg = "black", command = clickme )
    b3 = Button (topframe, text = "Button3", fg = "black", command = clickme )
    b4 = Button (topframe, text = "Button4", fg = "black", command = clickme )

    b1.pack(side = "left")
    b2.pack(side = "left")
    b3.pack(side = "left")
    b4.pack(side = "left")

    win.mainloop()
if __name__ == "__main__":
    main()
