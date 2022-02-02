# API-key: ac58a803
# Append to all requests sent to the API

# --- LOG ---
# Nils och Edvin:
# log startade 2/2 kl 10:30 -> 12:15

# Nils:

# Edvin:
# log startade 2/2 15:15 -> 15:30




import requests
import json
# param={"apikey":"ac58a803","i":"tt3896198"}
# link = "http://www.omdbapi.com/"
# result = requests.get(link,params=param)
# data=result.json()

# print(data)
# filename="request_data_id.json"
# with open(filename,"w",encoding="utf-8") as jsonfile:
#     jsonfile.write(json.dumps(data))
    
    
param={"apikey":"ac58a803","s":"star"}
link = "http://www.omdbapi.com/"
result = requests.get(link,params=param)
data=result.json()

print(data)
filename="request_data_search.json"
with open(filename,"w",encoding="utf-8") as jsonfile:
    jsonfile.write(json.dumps(data))


# PSEUDO MENY
# 
# 1. Söka efter film - resultat ska presenteras med kortfattad info av sökt film
#   EXTRA: 1.1. Välj film - om sökningen returnerar flera träffar ska användaren få välja film ur en lista
# 2. Visa senaste sökningar - programmet ska spara en historik av de senaste sökningarna (=< 5)
#   EXTRA: 2.1. Visa information om senaste sökta filmerna
#   EXTRA: 2.2. Visa information om vald sökt film
# 3. Avsluta
#
# Extra funktioner att bygga ut om vi vill och har tid:
# 1. Skapa klass som hanterar objekt av de sökta filmerna
# 2. Låt användaren sätta egna betyg på sökta filmer (spara film och betyg i en jsonfil)
# 3. Utöka med ytterligare funktionalitet (dokumentation om apiet finns på http://www.omdbapi.com/)
# 4. Visa en poster på filmen med hjälp av t ex Pillow
# 5. Skapa ett gui-program med hjälp av TKinter istället för ett konsolprogram