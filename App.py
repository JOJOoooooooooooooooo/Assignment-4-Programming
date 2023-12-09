from tkinter import *
import os
from tkinter import ttk

#genre_title = Label(movie_genre_time, text= "Genre")
#genre_combobox = ttk.Combobox(movie_genre_time, values = ["Horror", "Comedy", "Action", "Adventure", "Fantasy", "Sci-fi", "Romance", "Thriller", "Drama"])

#time_title = Label(movie_genre_time, text= "Duration In Hours")
#time_spinbox = Spinbox(movie_genre_time, from_= 0, to = 4)

#minutes_title = Label(movie_genre_time, text= "Duration in Minutes")
#minutes_entry = Entry(movie_genre_time)

def Start():
    win.destroy()
    global win2
    win2 = Tk()
    win2.title("Movie Library")
    win2.geometry("700x300")
    frame = Frame(win2)
    frame.pack()

    #Saving User input of Movie information
    movie_info_frame = LabelFrame(frame, text= "Movie Information")
    movie_info_frame.grid(row=0, column= 0)

    name_of_movie_label = Label(movie_info_frame, text= "Movie Name")
    name_of_movie_label.grid(row= 0, column= 0)

    name_of_director_label =Label(movie_info_frame, text= "Name of Director")
    name_of_director_label.grid(row= 0, column= 1)

    movie_name_entry = Entry(movie_info_frame)
    movie_name_entry.grid(row=1, column= 0)

    director_name_entry = Entry(movie_info_frame)
    director_name_entry.grid(row=1 , column= 1)

    movie_id_label = Label(movie_info_frame, text= "Movie Id")
    movie_id_label.grid(row= 0, column= 2)

    movie_id_entry = Entry(movie_info_frame)
    movie_id_entry.grid(row=1, column= 2)

    for widget in movie_info_frame.winfo_children():
        widget.grid_configure(padx= 15, pady= 5)
    
    #Creating second box of info
    movie_genre_time

def Mainscreen():
    global win
    win = Tk()
    win.title("JOJO's Library")
    win.geometry( "700x300")
    frame = Frame(win)
    frame.pack()
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