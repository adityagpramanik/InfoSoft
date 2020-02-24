from tkinter import messagebox

def new_exit ():
    MsgBox = messagebox.askquestion ("Exiting", "Are you sure to want to exit?", icon = "warning")
    if MsgBox == "yes":
        exit()
