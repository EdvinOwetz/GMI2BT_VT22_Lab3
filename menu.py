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
        except json.JSONDecodeError:
            pass
        self.show_menu()
    
    def frame_text(self,text:str):
        text=text.split("\n")
        text_len=0
        for line in text:
            text_len=max(text_len,len(line))
        if text_len % 2 != 0:
            text_len+=1
        dashes=text_len+2
        print("\n","-"*dashes)
        for lines in text:
            print("|",lines.ljust().rjust(int(text_len/2)),"|")
        print("-"*dashes,end="\n\n")
    
    def show_menu(self):
        try:
            while True:
                print("\n----------------------------------------------------")
                print("|                  GMI2BT - Lab 3                  |")
                print("| Nils Broberg (h19nilbr) & Edvin Owetz (h20edvow) |")
                print("----------------------------------------------------\n")
                #self.frame_text("GMI2BT - Lab 3\nNils Broberg (h19nilbr) & Edvin Owetz (h20edvow)")
                print(" 1) Sök film")
                print(" 2) Visa de senaste sökningarna")
                print(" 3) Avsluta programmet")
                #print(" FLERA MENYVAL HÄR ")
                #print(" FLERA MENYVAL HÄR ")
                #print(" FLERA MENYVAL HÄR ")
                #print(" FLERA MENYVAL HÄR ")
                try:
                    menu_input = int(input("\nVälj ett alternativ: "))
                except ValueError:
                    continue
                if menu_input == 1:
                    movie_search(self.history)
                elif menu_input == 2:
                    show_history(self.history)
                elif menu_input == 3:
                    print("\nAvslutar...")
                    break
                else:
                    print("Error: Felaktigt val!")
        except KeyboardInterrupt:
            print("\nAvslutar...")
        finally:
            self.history.save()
        
            