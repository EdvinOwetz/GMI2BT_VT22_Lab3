# A file containing error messages to be used accross the program

def no_result():
    print("\nSökningen gav inga resultat! Prova att söka efter en annan titel.")

def history_empty():
    print("\nDet finns inga sökningar sparade!")

def input_int(input_text, error_text = "\nFel värde inmatat, försök igen!") -> int:
    while True:
        try:
            num = int(input(input_text))
            return num
        except ValueError:
            print(error_text)

def menu_invalid_opt():
    print("\nFelaktigt menyval, försök igen!")