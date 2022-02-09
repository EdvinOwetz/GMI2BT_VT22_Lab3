from apihandler import APIhandler , APICallResponseEmpty
from movie import Movie
from history import History
#from common import 
# A file containing methods and functions

# Sök på film

# Visa sökhistorik (senaste)
    # Returnera en lista vari användaren kan välja index och visa mer info om vald film



def movie_search(history:History) -> None:
    search = input("\nAnge en sökterm: ")
    try:
        movie_list = APIhandler.general_search_to_movie_list(search)
        chosen_movie = choose_movie(movie_list)
        history.add_movie(chosen_movie)
        show_movie(chosen_movie)
    except APICallResponseEmpty:
        print("Hittade inte filmen!")

def show_history(history:History) -> None:
    listan = history.history_list
    the_movie = choose_movie(listan)
    show_movie(the_movie)

def choose_movie(movie_list:list[Movie]) -> Movie:
    if len(movie_list)==0:
        print("Error, nothing in list")
        return
    elif len(movie_list)==1:
        return movie_list[0]

    for index in range(len(movie_list)):
        print(f"{str(index+1).ljust(2)}: {movie_list[index].title} , {movie_list[index].year}")
    while True:
        try:
            choose = int(input("\nAnge en filmnummer i listan: "))
        except ValueError:
            continue
        if choose >=0 or choose <len(movie_list):
            break
        else:
            print("Fel index")
    return movie_list[choose - 1]
    #tar in en lista med movies 
    #väljen
    #returnerna den

def show_movie(movie:Movie) -> None:
    
    #sök på id
    #Movie objectet.get_details()
    #visa resultat på lämpligt sätt?
    movie_dict=movie.get_details()
    movie_text=f"Titel: {movie_dict['Title']}\n"
    movie_text += f"Released: {movie_dict['Released']}\n"
    movie_text += f"Runtime: {movie_dict['Runtime']}\n"
    movie_text += f"Genre: {movie_dict['Genre']}\n"
    movie_text += f"Director: {movie_dict['Director']}\n"
    movie_text += f"Actors: {movie_dict['Actors']}\n"
    movie_text += f"Country: {movie_dict['Country']}\n"
    movie_text += f"Language: {movie_dict['Language']}\n"
    movie_text += f"Imdb rating: {movie_dict['imdbRating']}\n"
    movie_text += f"Summary of the plot: {movie_dict['Plot']}\n"
    print("\n", movie_text)