from tkinter import *
import os


def Start():
    win.destroy()
    global win2
    win2 = Tk()
    win2.title("Movie Library")
    win2.geometry("700x300")

    


def Mainscreen():
    global win
    win = Tk()
    win.title("JOJO's Library")
    win.geometry( "700x300")
    Title_Lable = Label(text= "Welcome to JOJO's Movie Library", font= ("Calibri, 13"))
    Title_Lable.pack()
    Label(text= "").pack()

    Label(text= "").pack()
    Label(text= "").pack()
    Start_Button = Button(text= "Start", height= "2", width= "25", command= Start)
    Start_Button.pack()
    Label(text= "").pack()
    Exit_Button = Button(text= "Exit", height= "2", width= "25", command= win.destroy)
    Exit_Button.pack()


    
    win.mainloop()

Mainscreen()