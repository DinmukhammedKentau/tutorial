import json
def connection():
    with open("data.json","r")as file:
        movies = json.load(file)
        moviesList = movies ["movies"]
        file.close()
    return moviesList
def avg(movies):
   count = 0
   sum = 0
   for movie in movies:
       count+=1
       sum+=movie["imdb"]
   return sum/count

print(avg(connection()))