import json
from movie import Movie

#lista med HistoryEntries

#funktioner för att ladda och spara historiken
class History:
    
    def __init__(self,filename="history.json"):
        self.history_list:list[Movie]=[]
        self.filename=filename

    def add_movie(self,movie:Movie)->None:
        self.history_list.insert(0,movie)
        
    def remove_movie(self,movie:Movie)->None:
        self.history_list.remove(movie)
    
    def to_dict(self)->dict:
        print(self.history_list)
        print({"History":[item.to_dict() for item in self.history_list]})
        return {"History":[item.to_dict() for item in self.history_list]}
    
    def save(self)->None:
        if len(self.history_list) != 0:
            with open(self.filename,"w",encoding="utf-8") as file:
                file.write(json.dumps(self.to_dict()))
    
    def load(self)->None:
        with open(self.filename,"r",encoding="utf-8") as file:
            self.history_list=json.loads(file.read())
            print(self.history_list)
            self.history_list=self.history_list["History"]
            print(self.history_list)
            self.history_list=[item self.history_list]
            #hantera tom json
    
    def print_str(self)->str:
        pass