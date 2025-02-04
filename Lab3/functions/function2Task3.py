import json
def boevik(movies,b):
    sublist=[]
    for movie in movies:
        if(movie["category"]==b):
            sublist.append(movie)
    return sublist

def connection():
    with open("data.json","r") as file:
        movies = json.load(file)
        moviesList = movies["movies"]
        file.close()
    return moviesList
a=input("Category ait")
movies=connection()
print(boevik(movies,a))