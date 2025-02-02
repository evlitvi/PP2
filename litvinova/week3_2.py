# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
def is_IMDB_above_5_5(movie):
    return movie["imdb"]>5.5

print(is_IMDB_above_5_5(movies[-2]))

#2
def imdb_above_5_5(movies):
    goodMovies = []
    for movie in movies:
        if movie["imdb"]>5.5:
            goodMovies.append(movie["name"])
    return goodMovies
            
print(imdb_above_5_5(movies))

#3
movieCategory = input()

def getByCategory(category, movies):
    byCategory = []
    for movie in movies:
        if movie["category"] == category:
            byCategory.append(movie)
    return byCategory

print(getByCategory(movieCategory, movies))

#4
def avgMovieScore(movies):
    avgScore=0
    for movie in movies:
        avgScore+=movie["imdb"]
    return avgScore/len(movies)

print(avgMovieScore(movies))

#5
movieCategory2 = input()
def avgScoreByCategory(category, movies):
    return avgMovieScore(getByCategory(category, movies))

print(avgScoreByCategory(movieCategory2, movies))