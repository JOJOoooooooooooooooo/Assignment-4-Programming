from tkinter import *
import os
from tkinter import ttk






def Start():
    win.destroy()
    global win2
    win2 = Tk()
    win2.title("Movie Library")
    win2.geometry("600x500")
    frame = Frame(win2)
    frame.pack()

    #Saving User input of Movie information
    movie_info_frame = LabelFrame(frame, text= "Movie Information")
    movie_info_frame.grid(row=0, column= 0, sticky="news", padx=20, pady=20)

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
    movie_genre_time_frame = LabelFrame(frame, text= "Movie Genre & Time")
    movie_genre_time_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

    genre_title = Label(movie_genre_time_frame, text= "Genre")
    genre_title.grid(row= 3, column= 1)
    genre_combobox = ttk.Combobox(movie_genre_time_frame, values = ["Horror", "Comedy", "Action", "Adventure", "Fantasy", "Sci-fi", "Romance", "Thriller", "Drama"])
    genre_combobox.grid(row= 4, column= 1)

    time_title = Label(movie_genre_time_frame, text= "Duration In Hours")
    time_title.grid(row= 3, column= 2)
    time_spinbox = Spinbox(movie_genre_time_frame, from_= 0, to = 4)
    time_spinbox.grid(row= 4, column= 2)

    minutes_title = Label(movie_genre_time_frame, text= "Duration in Minutes")
    minutes_title.grid(row=3, column= 3)
    minutes_entry = Entry(movie_genre_time_frame)
    minutes_entry.grid(row=4, column=3)

    for widget in movie_genre_time_frame.winfo_children():
        widget.grid_configure(padx= 15, pady= 5)
    
    movie_rating_frame = LabelFrame(frame, text= "Movie Rating & Recommendation")
    movie_rating_frame.grid(row=2, column= 0, sticky="news", padx=20, pady= 20)

    rating_title = Label(movie_rating_frame, text= "Rating")
    rating_title.grid(row= 0, column= 0)

    rating_combobox = ttk.Combobox(movie_rating_frame, values= ["0","0.5", "1","1.5","2","2.5","3", "3.5", "4", "4.5", "5", "5.5", "6", "6.5", "7", "7.5", "8", "8.5", "9", "9.5", "10"])
    rating_combobox.grid(row=1, column=0)

    recommendation_lebel = Label(movie_rating_frame, text="Recommendation")
    recommendation_lebel.grid(row=0, column= 1)

    recommendation_checkbox = Checkbutton(movie_rating_frame, text="Would you recommend this movie?")
    recommendation_checkbox.grid(row=1, column=1)

    for widget in movie_rating_frame.winfo_children():
        widget.grid_configure(padx= 15, pady= 5)

    #Adding "Add Movie" Button




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