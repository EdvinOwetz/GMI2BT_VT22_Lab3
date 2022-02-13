class Movie:
    
    def __init__(self, json_dict: str) -> None:
        self.title = json_dict["Title"]
        self.year = json_dict["Year"]
        self.imdb_id = json_dict["imdbID"]

    def get_details(self) -> dict:
        from apihandler import APIhandler
        return APIhandler.id_search(self.imdb_id)

    def to_dict(self) -> dict:
        return {"Title": self.title, "Year": self.year, "imdbID": self.imdb_id}