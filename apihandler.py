import requests
from movie import Movie

class APICallResponseEmpty(Exception):
    pass

class APIhandler:

    apikey = "ac58a803"

    @staticmethod
    def id_search(search):
        """Search movie by id, using searchparameter \"i\" in omdb-api."""
        param = {"apikey": APIhandler.apikey, "i": search}
        link = "http://www.omdbapi.com/"
        result = requests.get(link, params=param)
        data = result.json()
        return data

    @staticmethod
    def general_search(search):
        """Search movies by title, using searchparameter \"s\" in omdb-api."""
        param = {"apikey": APIhandler.apikey, "s": search}
        link = "http://www.omdbapi.com/"
        result = requests.get(link, params=param)
        data = result.json()
        return data

    @staticmethod
    def general_search_to_movie_list(search):
        movie_list_dict = APIhandler.general_search(search)
        if movie_list_dict["Response"] == "False":
            raise(APICallResponseEmpty)
        return [Movie(item) for item in movie_list_dict["Search"]]
