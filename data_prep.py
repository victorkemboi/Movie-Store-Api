import json

with open('movie_list.json','r' , encoding='utf-8') as movie_list:
    data = json.load(movie_list)
    for movie  in data:
   
        newCast = []
    
        for actor in movie['cast']:
            newActor = {}
            newActor["name"] = actor
            newCast.append(newActor)
        
        movie['cast'] = newCast

        newGenres= []
        for genre in movie['genres']:
            newGenre = {}
            newGenre["genre"] = genre
            newGenres.append(newGenre)
        
        movie['genres'] = newGenres
 
    with open('data_prepped.json', 'w') as write_file:
             json.dump( data, write_file)

             write_file.close()

    movie_list.close()
   
