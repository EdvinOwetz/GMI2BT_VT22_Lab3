import json
from movie import Movie

class CouldNotLoadFile(Exception):
    pass

class History:

    def __init__(self, filename="history.json"):
        self.history_list: list[Movie] = []
        self.filename = filename

    def add_movie(self, movie: Movie) -> None:
        self.history_list.insert(0, movie)

    def remove_movie(self, movie: Movie) -> None:
        self.history_list.remove(movie)

    def to_dict(self) -> dict:
        return {"History": [item.to_dict() for item in self.history_list]}

    def save(self) -> None:
        if len(self.history_list) != 0:
            with open(self.filename, "w", encoding="utf-8-sig") as file:
                file.write(json.dumps(self.to_dict(),
                           indent = 4, ensure_ascii = False))

    def load(self) -> None:
        try:
            with open(self.filename, "r", encoding="utf-8-sig") as file:
                self.history_list = [
                    Movie(item) for item in json.loads(file.read())["History"]]
        except:
            raise(CouldNotLoadFile)