from history import History
import json

from modules import movie_search,show_history
class Menu:
    def __init__(self):
        self.history = History()
        try:
            self.history.load()
        except FileNotFoundError:
            print("Hittade ingen \"",self.history.filename,"\" fil.")
        self.show_menu()
        
    
    def frame_text(self,text:str,h_padding:int=1,h_char:str="-",v_char:str="|"):
        text=text.split("\n")
        text_len=0
        for line in text:
            text_len=max(text_len,len(line))
        text_len += h_padding*2
        dashes = h_char * (text_len + 2)
        print("\n"+dashes)
        for line in text:
            space=text_len-len(line)
            print(v_char+(" "*int(space/2))+line+(" "*int(round(space/2,0)))+v_char)
        print(dashes,end="\n\n")
    
    def show_menu(self):
        error_text="Error: Felaktigt val!"
        while True:
            # print("\n----------------------------------------------------")
            # print("|                  GMI2BT - Lab 3                  |")
            # print("| Nils Broberg (h19nilbr) & Edvin Owetz (h20edvow) |")
            # print("----------------------------------------------------\n")
            self.frame_text("GMI2BT - Lab 3\nNils Broberg (h19nilbr) & Edvin Owetz (h20edvow)")
            print(" 1) Sök film")
            print(" 2) Visa de senaste sökningarna")
            print(" 3) Avsluta programmet")
            try:
                menu_input = int(input("\nVälj ett alternativ: "))
            except ValueError:
                print(error_text)
                continue
            except KeyboardInterrupt:
                print("\nAvslutar...")
                break
            if menu_input == 1:
                movie_search(self.history)
            elif menu_input == 2:
                show_history(self.history)
            elif menu_input == 3:
                print("\nAvslutar...")
                break
            else:
                print(error_text)
        self.history.save()
        
            