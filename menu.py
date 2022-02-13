from history import History, CouldNotLoadFile
from apihandler import APIhandler, APICallResponseEmpty
from movie import Movie
from common import input_int, history_empty, menu_invalid_opt, no_result


class Menu:
    def __init__(self):
        self.history = History()
        try:
            self.history.load()
        except CouldNotLoadFile:
            print("Fel vid linläsning av \"",
                  self.history.filename, "\" filen.")
        self.show_menu()

    def frame_text(self, text: str, h_padding: int = 1, h_char: str = "-", v_char: str = "|"):
        text = text.split("\n")
        text_len = 0
        for line in text:
            text_len = max(text_len, len(line))
        text_len += h_padding * 2
        dashes = h_char * (text_len + 2)
        print("\n" + dashes)
        for line in text:
            space = text_len - len(line)
            print(v_char + (" "*int(space/2)) + line +
                  (" " * int(round(space/2, 0))) + v_char)
        print(dashes, end = "\n\n")

    def show_menu(self):
        try:
            while True:
                self.frame_text(
                    "GMI2BT - Lab 3\nNils Broberg (h19nilbr) & Edvin Owetz (h20edvow)")
                print(" 1) Sök film")
                print(" 2) Visa de senaste sökningarna")
                print(" 3) Avsluta programmet")
                menu_input = input_int("\nVälj ett alternativ: ")
                if menu_input == 1:
                    self.movie_search()
                elif menu_input == 2:
                    self.show_history()
                elif menu_input == 3:
                    print("\nAvslutar...")
                    break
                else:
                    menu_invalid_opt()
        except KeyboardInterrupt:
            print("\nAvslutar...")
        self.history.save()
        
    def movie_search(self) -> None:
        search = input("\nAnge en sökterm: ")
        try:
            movie_list = APIhandler.general_search_to_movie_list(search)
            chosen_movie = self.choose_movie(movie_list)
            self.history.add_movie(chosen_movie)
            self.show_movie(chosen_movie)
        except APICallResponseEmpty:
            no_result()

    def show_history(self) -> None:
        listan = self.history.history_list
        if len(listan) == 0:
            history_empty()
            return
        the_movie = self.choose_movie(listan)
        self.show_movie(the_movie)

    def choose_movie(self,movie_list: list[Movie]):
        if len(movie_list) == 1:
            return movie_list[0]
        for index in range(len(movie_list)):
            print(
                f"{str(index+1).ljust(2)}: {movie_list[index].title} , {movie_list[index].year}")
        while True:
            choose = input_int("\nAnge en filmnummer i listan: ")
            if choose >= 0 or choose < len(movie_list):
                break
            menu_invalid_opt()
        return movie_list[choose - 1]

    def show_movie(self,movie: Movie) -> None:
        movie_dict = movie.get_details()
        movie_text = f"Titel: {movie_dict['Title']}\n"
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