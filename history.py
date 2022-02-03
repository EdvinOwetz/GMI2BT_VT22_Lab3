from historyentry import HistoryEntry
from movie import Movie

#lista med HistoryEntries

#funktioner för att ladda och spara historiken
class History:
    
    def __init__(self,filename="history.json"):
        self.history_list:list[Movie]=[]
        self.filename=filename
    
    def to_dict(self)->dict:
        pass
    
    def save(self)->None:
        pass
    
    def load(self)->None:
        pass
    
    def print(self)->str:
        
        pass