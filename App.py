from tkinter import *
import os
from tkinter import ttk
from tkinter import messagebox
import csv


def find_movie():
    win2.destroy()
    win3= Tk()
    win3.title("Find My Movie")
    win3.geometry("900x400")
    frame = Frame(win3)
    frame.pack()

    file = open('Movies.csv')
    Reader = csv.reader(file)
    Data = list(Reader)
    
    list_of_entries = []
    for x in list(range(0,len(Data))):
        list_of_entries.append(Data[x][0])

    list_of_movies_frame = LabelFrame(frame, text= "List of Movies")
    list_of_movies_frame.grid(row=0 , column=0)

    global listbox1
    var = StringVar(value = list_of_entries)
    listbox1 = Listbox(list_of_movies_frame, listvariable= var)
    listbox1.grid(row=1, column=0, padx= 15)

    def update():
        index = listbox1.curselection()[0]
        movie_name_label1.config(text= Data[index][0])
        Director_name_label1.config(text= Data[index][1])
        movie_id_label1.config(text= Data[index][2])
        Genre_label1.config(text= Data[index][3])
        time_in_hrs_label1.config(text= Data[index][4])
        time_in_mins_label1.config(text= Data[index][5])
        rating_label1.config(text= Data[index][6])
        recommend_label1.config(text= Data[index][7])
        return None

    update_button = Button(list_of_movies_frame, text= "Update", command = update)
    update_button.grid(row=1, column=2)

    id_label = Label(list_of_movies_frame, text="Movie ID")
    id_label.grid(row=0, column=2, padx=15)

    id_entry = Entry(list_of_movies_frame)
    id_entry.grid(row=0, column=3, padx=15)
    
    def find_by_id():
        movie_id = id_entry.get()
        for index, movie in enumerate(Data):
            if str(movie[2]) == str(movie_id):
                listbox1.selection_clear(0, END)
                listbox1.selection_set(index)
                listbox1.activate(index)
                update()
                break
        else:
            messagebox.showwarning("Movie Not Found", "No movie found with the specified ID.")
        update()

    find_button = Button(list_of_movies_frame, text="Find by ID", command= find_by_id)
    find_button.grid(row=1,column=3,padx= 15)

    movie_name_label = Label(frame, text= "Movie Name")
    movie_name_label.grid(row=0, column=2, sticky= 'w', padx= 15)
    Director_name_label = Label(frame, text= "Director Name")
    Director_name_label.grid(row=1, column=2, sticky= 'w', padx= 15)
    movie_id_label = Label(frame, text= "Movie Id")
    movie_id_label.grid(row=2, column=2, sticky= 'w', padx= 15)
    Genre_label = Label(frame, text= "Genre")
    Genre_label.grid(row=3, column=2, sticky= 'w', padx= 15)
    time_in_hrs_label = Label(frame, text= "Time in (Hrs)")
    time_in_hrs_label.grid(row=4, column=2, sticky= 'w', padx= 15)
    time_in_mins_label = Label(frame, text= "Time in (Mins)")
    time_in_mins_label.grid(row=5, column=2, sticky= 'w', padx= 15)
    rating_label = Label(frame, text= "Rating")
    rating_label.grid(row=6, column=2, sticky= 'w', padx= 15)
    recommend_label = Label(frame, text= "Recommendation")
    recommend_label.grid(row=7, column=2, sticky= 'w', padx= 15)

    movie_name_label1 = Label(frame, text= "")
    movie_name_label1.grid(row=0, column=3, sticky= 'w', padx= 15)
    Director_name_label1 = Label(frame, text= "")
    Director_name_label1.grid(row=1, column=3, sticky= 'w', padx= 15)
    movie_id_label1 = Label(frame, text= "")
    movie_id_label1.grid(row=2, column=3, sticky= 'w', padx= 15)
    Genre_label1 = Label(frame, text= "")
    Genre_label1.grid(row=3, column=3, sticky= 'w', padx= 15)
    time_in_hrs_label1 = Label(frame, text= "")
    time_in_hrs_label1.grid(row=4, column=3, sticky= 'w', padx= 15)
    time_in_mins_label1 = Label(frame, text= "")
    time_in_mins_label1.grid(row=5, column=3, sticky= 'w', padx= 15)
    rating_label1 = Label(frame, text= "")
    rating_label1.grid(row=6, column=3, sticky= 'w', padx= 15)
    recommend_label1 = Label(frame, text= "")
    recommend_label1.grid(row=7, column=3, sticky= 'w', padx= 15)

    def save_to_csv():
        with open('Movies.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(Data)
            
            
    def delete():
        index = listbox1.curselection()[0]

        listbox1.delete(index)

        del Data[index]

        for label in [movie_name_label1, Director_name_label1, movie_id_label1,Genre_label1, time_in_hrs_label1, time_in_mins_label1, rating_label1, recommend_label1]:
            label.config(text="")

        save_to_csv()
    def edit():
        index = listbox1.curselection()[0]
        current_data = Data[index]

        edit_win = Toplevel()
        edit_win.title("Edit Movie Selection")
        edit_win.geometry("550x400")

        new_movie_name_entry = Entry(edit_win, width=30)
        new_movie_name_entry.grid(row=0, column=1, padx=10, pady=5)
        new_director_entry = Entry(edit_win, width=30)
        new_director_entry.grid(row=1, column=1, padx=10, pady=5)
        new_genre_entry = ttk.Combobox(edit_win, width=30, values = ["Horror", "Comedy", "Action", "Adventure", "Fantasy", "Sci-fi", "Romance", "Thriller", "Drama"])
        new_genre_entry.grid(row=2, column=1, padx=10, pady=5)
        new_duration_hrs = Spinbox(edit_win, width=30, from_= 0, to = 4)
        new_duration_hrs.grid(row=3, column=1,padx=10, pady=5)
        new_duration_mins = Entry(edit_win, width=30)
        new_duration_mins.grid(row=4, column=1, padx=10, pady=5)
        new_rating_entry = ttk.Combobox(edit_win, values= ["0","0.5", "1","1.5","2","2.5","3", "3.5", "4", "4.5", "5", "5.5", "6", "6.5", "7", "7.5", "8", "8.5", "9", "9.5", "10"])
        new_rating_entry.grid(row=5, column=1, padx=10, pady=5)

        Label(edit_win, text="New Movie Name:").grid(row=0, column=0, padx=10, pady=5)
        Label(edit_win, text="New Director Name:").grid(row=1, column=0, padx=10, pady=5)
        Label(edit_win, text="New Genre").grid(row=2, column=0, padx=10, pady=5)
        Label(edit_win, text="New Duration in Hrs").grid(row=3, column=0, padx=10, pady=5)
        Label(edit_win, text="New Duration in Mins").grid(row=4, column=0, padx=10, pady=5)
        Label(edit_win, text="New Rating").grid(row=5, column=0, padx=10, pady=5)

        def apply_edit():
            current_data[0] = new_movie_name_entry.get() if new_movie_name_entry.get() else current_data[0]
            current_data[1] = new_director_entry.get() if new_director_entry.get() else current_data[1]
            current_data[3] = new_genre_entry.get() if new_genre_entry.get() else current_data[3]
            current_data[4] = new_duration_hrs.get() if new_duration_hrs.get() else current_data[4]
            current_data[5] = new_duration_mins.get() if new_duration_mins.get() else current_data[5]
            current_data[6] = new_rating_entry.get() if new_rating_entry.get() else current_data[6]

            listbox1.delete(index)
            listbox1.insert(index, current_data[0])

            save_to_csv()

            edit_win.destroy()

        apply_button = Button(edit_win, text="Apply", command=apply_edit)
        apply_button.grid(row=10, column=0, columnspan=2, pady=10)
        

    delete_button = Button(frame, text="Delete", command= delete)
    delete_button.grid(row=8, column= 3)

    edit_button = Button(frame, text="Edit", command= edit)
    edit_button.grid(row=8, column= 2)



    
#user info
def add_movie():
    movie_name = movie_name_entry.get()
    director_name = director_name_entry.get()
    movie_id = movie_id_entry.get()
    Genre = genre_combobox.get()
    time_hrs = time_spinbox.get()
    time_mins = minutes_entry.get()
    rating = rating_combobox.get()
    Recommendation = rec_status_var.get()

    if movie_name and director_name and movie_id and Genre and time_hrs and time_mins and rating and Recommendation:
        data_to_append = [
            [movie_name, director_name, movie_id, Genre, time_hrs, time_mins, rating, Recommendation]
    ]
        file = open('Movies.csv', 'a', newline= '')
        writer = csv.writer(file)

        writer.writerows(data_to_append)

        file.close()

        movie_name_entry.delete(0, END)
        director_name_entry.delete(0, END)
        movie_id_entry.delete(0, END)
        genre_combobox.set("")  # Set to an empty string or a default value
        time_spinbox.delete(0, END)  # Assuming you want to clear the Spinbox value
        minutes_entry.delete(0, END)
        rating_combobox.set("")  # Set to an empty string or a default value
        rec_status_var.set("Not Recommended")
        
        print("Movie name:", movie_name, " Director Name:", director_name, "Movie Id:", movie_id)
        print("Genre:", Genre, " Time(Hrs):", time_hrs, " Minutes:", time_mins, " Rating:", rating)
        print("Recommendation:", Recommendation)

        messagebox.showinfo("Movie Added", "Movie successfully added!")
    else:
        messagebox.showerror(title="Error", message="All Variables Must be Added")


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

    global movie_id_entry
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