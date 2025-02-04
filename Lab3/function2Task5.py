import json
def connection():
    with open("data.json","r")as file:
        movies = json.load(file)
        movieList = movies["movies"]
        file.close()
    return movieList
def avgByCategory(category):
    count=0
    sum=0
    for movie in connection():
        if movie["category"]==category:
            count+=1
            sum+=movie["imdb"]
    print(sum/count)

categories = ("Romance","Thriller","Suspense","Comedy","War","Crime","Drama"
              ,"Adventure","Action")
for i in range(len(categories)):
    print(i,categories[i])
index=int(input("enter index of movie:"))
avgByCategory(categories[index])
