"""

Let's return to the music example from assignment one. Pick 3 of the attributes you listed. For our example we're going to say "Genre", "Artist" and "Year". 
Create a new Python file and create 3 functions with the same name as those attributes. So in this example we'd have one function named "genre" another named "artist" 
and another called "year".

When someone calls any of those functions, that function should return the corresponding value for that attribute. 
For example, if we call the "Artist" function our function would return "Dave Brubeck". Yours should return whatever values make sense for your music choice.

"""

Artist = "Future"
Genre = "Rap & HipHop"
Name = "Life is Good"

def artist(Name):
    Output = Artist
    return Output

def genre(Genre):
    Output = Genre
    return Output

def name(Name):
    Output = Name
    return Output



artname = artist(Artist)
print(artname)

songname = name(Name)
print(songname)

gentype = genre(Genre)
print(gentype)
