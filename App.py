from tkinter import *
import os
from tkinter import ttk
from tkinter import messagebox
import csv


def find_movie():
    win2.destroy()
    win3= Tk()
    win3.title("Find My Movie")
    win3.geometry("550x400")

    file = open('Movies.csv')
    Reader = csv.reader(file)
    Data = list(Reader)
    
    list_of_entries = []
    for x in list(range(0,len(Data))):
        list_of_entries.append(Data[x][0])

    var = StringVar(value = list_of_entries)
    listbox1 = Listbox(win3, listvariable= var)
    listbox1.pack()
    
    display_all_button = Button(text= "Display All")
    display_all_button.pack()
#user info
def add_movie():
    movie_name = movie_name_entry.get()
    director_name = director_name_entry.get()
    Genre = genre_combobox.get()
    time_hrs = time_spinbox.get()
    time_mins = minutes_entry.get()
    rating = rating_combobox.get()
    Recommendation = rec_status_var.get()

    data_to_append = [
        [movie_name, director_name, Genre, time_hrs, time_mins, rating, Recommendation]
]
    file = open('Movies.csv', 'a', newline= '')
    writer = csv.writer(file)

    writer.writerows(data_to_append)

    file.close()

    if movie_name and director_name:
        print("Movie name:", movie_name, " Director Name:", director_name)
        print("Genre:", Genre, " Time(Hrs):", time_hrs, " Minutes:", time_mins, " Rating:", rating)
        print("Recommendation:", Recommendation)
    else:
        messagebox.showerror(title="Error", message="Must State A Movie and Director Name ")


def Start():
    win.destroy()
    global win2
    win2 = Tk()
    win2.title("Movie Library")
    win2.geometry("550x400")
    frame = Frame(win2)
    frame.pack()

    #Saving User input of Movie information
    movie_info_frame = LabelFrame(frame, text= "Movie Information")
    movie_info_frame.grid(row=0, column= 0, sticky="news", padx=20, pady=10)

    name_of_movie_label = Label(movie_info_frame, text= "Movie Name")
    name_of_movie_label.grid(row= 0, column= 0)

    name_of_director_label =Label(movie_info_frame, text= "Name of Director")
    name_of_director_label.grid(row= 0, column= 1)

    global movie_name_entry
    movie_name_entry = Entry(movie_info_frame)
    movie_name_entry.grid(row=1, column= 0)

    global director_name_entry
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
    movie_genre_time_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

    global genre_combobox
    genre_title = Label(movie_genre_time_frame, text= "Genre")
    genre_title.grid(row= 3, column= 1)
    genre_combobox = ttk.Combobox(movie_genre_time_frame, values = ["Horror", "Comedy", "Action", "Adventure", "Fantasy", "Sci-fi", "Romance", "Thriller", "Drama"])
    genre_combobox.grid(row= 4, column= 1)

    global time_spinbox
    time_title = Label(movie_genre_time_frame, text= "Duration In Hours")
    time_title.grid(row= 3, column= 2)
    time_spinbox = Spinbox(movie_genre_time_frame, from_= 0, to = 4)
    time_spinbox.grid(row= 4, column= 2)

    global minutes_entry
    minutes_title = Label(movie_genre_time_frame, text= "Duration in Minutes")
    minutes_title.grid(row=3, column= 3)
    minutes_entry = Entry(movie_genre_time_frame)
    minutes_entry.grid(row=4, column=3)

    for widget in movie_genre_time_frame.winfo_children():
        widget.grid_configure(padx= 15, pady= 5)
    
    movie_rating_frame = LabelFrame(frame, text= "Movie Rating & Recommendation")
    movie_rating_frame.grid(row=2, column= 0, sticky="news", padx=20, pady= 10)

    rating_title = Label(movie_rating_frame, text= "Rating")
    rating_title.grid(row= 0, column= 0)

    global rating_combobox
    rating_combobox = ttk.Combobox(movie_rating_frame, values= ["0","0.5", "1","1.5","2","2.5","3", "3.5", "4", "4.5", "5", "5.5", "6", "6.5", "7", "7.5", "8", "8.5", "9", "9.5", "10"])
    rating_combobox.grid(row=1, column=0)

    recommendation_lebel = Label(movie_rating_frame, text="Recommendation")
    recommendation_lebel.grid(row=0, column= 1)

    global rec_status_var
    rec_status_var = StringVar(value="Not Recommended")
    recommendation_checkbox = Checkbutton(movie_rating_frame, text="Would you recommend this movie?",
                                           variable= rec_status_var, onvalue="Recomended", offvalue="Not Recommended")
    recommendation_checkbox.grid(row=1, column=1)

    for widget in movie_rating_frame.winfo_children():
        widget.grid_configure(padx= 15, pady= 5)

    #Adding "Add Movie" Button
    add_movie_button = Button(frame, text= "Add Movie", command= add_movie)
    add_movie_button.grid( row=3, column=0)

    #Adding "Find Movie" Button
    find_movie_button = Button(frame,text="Find a Movie", command= find_movie)
    find_movie_button.grid (row= 4, column= 0, pady=10)

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