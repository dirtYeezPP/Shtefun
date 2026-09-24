class Film: 
    def __init__(self, title, rating):
        self.title = title 
        self.rating = rating 
    def __str__(self):
        return f"{self.title} has a rating of {self.rating}" 

mov1 = Film("Spirited away", 9.5)
mov2 = Film("A whisker away", 8.5)
movies = []
movies.append(mov1)
movies.append(mov2)

for mov in movies: 
    print(mov)

