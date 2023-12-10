#Find all Data

#update data,  Id Cannot be modifyiable 

#search and delete

#display all


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



    