from tkinter import *
import modules.messages as messages
import modules.tk_win as tk_win
import modules.tk_frame as tk_frame
import modules.tk_button as tk_button
import modules.tk_label as tk_label

# window creation
def main ():
    win = Tk()

    win.title("InfoSoft")
    win.iconbitmap("main.ico")
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

    b1 = Button (topframe, text = "Window ", fg = "black", command = tk_win.winfun, relief = "raised", bd = "3")
    b2 = Button (topframe, text = "Frame", fg = "black", command = tk_frame.framefun, relief = "raised", bd = "3")
    b3 = Button (topframe, text = "Label", fg = "black", command = tk_label.labelfun, relief = "raised", bd = "3")
    b4 = Button (topframe, text = "Button", fg = "black", command = tk_button.butfun, relief = "raised", bd = "3")
    exit_button = Button (bottomframe, text = "Exit", fg = "black", command = messages.new_exit)

    b1.pack(padx = "10", pady = "10", side = "left")
    b2.pack(padx = "10", pady = "10", side = "left")
    b3.pack(padx = "10", pady = "10", side = "left")
    b4.pack(padx = "10", pady = "10", side = "left")
    exit_button.pack()

    win.mainloop()
if __name__ == "__main__":
    main()
