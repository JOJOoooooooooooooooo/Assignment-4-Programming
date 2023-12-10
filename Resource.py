
#Data entered

def save_to_csv():
        with open('Movies.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(Data)
            