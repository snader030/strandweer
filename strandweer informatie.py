print("\n")
msg = "Welkom bij strandweer informatie"
print(msg)
print("\n")
# bestand plaatsnamen.txt wordt geopend om te lezen met de read-method
my_file = open("plaatsnamen.txt", "r")
# inhoud van bestand wordt gelezen en opgeslagen als string variabele genaamd "content"
content = my_file.read()
# inhoud van string variabele genaamd "content" wordt gesplitst en opgeslagen als list variabele genaamd "lijst_met_plaatsnamen"
lijst_met_plaatsnamen = content.split(",")
# bestand plaatsnamen.txt wordt gesloten
my_file.close()
# list variabele genaamd "lijst_met_plaatsnamen" wordt geprint
##print(lijst_met_plaatsnamen)

import inquirer

questions = [
    inquirer.List(
        "Plaatsnaam_keuze",
        message="Beste gebruiker, kies een badplaats d.m.v pijltjestoetsen en enter om een keuze te maken",
        choices=(lijst_met_plaatsnamen),
    ),
]
answers = inquirer.prompt(questions)
q = answers["Plaatsnaam_keuze"]

import requests
import json

appid = "a7f9e1a6b04a8b787e857547840c3a36"
url = (
    "https://api.openweathermap.org/data/2.5/forecast?q=%s&appid=%s&units=metric&cnt=5"
    % (
        q,
        appid,
    )
)

response = requests.get(url)
data = json.loads(response.text)

temp0 = data["list"][0]["main"]["feels_like"]
temp1 = data["list"][1]["main"]["feels_like"]
temp2 = data["list"][2]["main"]["feels_like"]
temp3 = data["list"][3]["main"]["feels_like"]
temp4 = data["list"][4]["main"]["feels_like"]

##print(("De hoogste temperatuur is:"), (max(temp0, temp1, temp2, temp3, temp4),))

# Print extra witregel voor leesbaarheid
print(" ")

# defineer graden teken voor graden Celcius
degree_sign = u"\N{DEGREE SIGN}"

# Print onderstaande
print(
    ("De verwachte temperaturen voor de komende vijf dagen zijn:"),
    (temp0, temp1, temp2, temp3, temp4),
)

# Maak integer variabele aan met als waarde de hoogste waarde van temp0 t/m temp4
maxtemp = max(temp0, temp1, temp2, temp3, temp4)

# Print onderstaande
print(("De hoogste verwachte temperatuur is:"), (maxtemp), (degree_sign), "C")

# Maak lijst-variabele aan met daarin de 5 temperaturen
lijst_temp_van_5_dagen = [temp0, temp1, temp2, temp3, temp4]

# Maak integer variabele aan met als waarde het index nummer van de positie van de hoogste waarde in de lijst variabele lijst_temp_van_5_dagen
# Ieder element uit een Python list heeft een 'eigen' nummer; een index nummer. Het eerste index
# nummer is altijd een 0 en het volgende nummer is steeds één integer hoger, dus 0,1,2,3 enz)
# Zie https://www.kite.com/python/answers/how-to-find-the-index-of-the-max-value-in-a-list-in-python
# The max value in a list is the element with the highest value. Finding the index of the max value in
# a list returns the position of the max value within the list.
max_index = lijst_temp_van_5_dagen.index(maxtemp)

# Print ter controle het indexnummer
print(
    ("het index nummer van de positie van de hoogste waarde in de lijst is:"),
    (max_index),
)
# Omdat de lijst begint met element 0
# Maak integer variabele aan die de waarde heeft van het index nr van de dag met de hoogste temp verhoogd met 1
dag_met_max_temp = max_index + 1

# Converteer de integer variabele naar een string variabele (change variable type), anders kan dit niet
# omdat het twee verschillende variable types zijn, namelijk string en integer: max_index_str + "e dag")
# Zie https://www.geeksforgeeks.org/convert-integer-to-string-in-python/
max_index_str = str(dag_met_max_temp)

# Print ter controle de string variabele
print(("Dit is positie"), (max_index_str))

# Print onderstaande
print(("Dit is dus op de"), (max_index_str + "e dag"))

# Print onderstaande
print(("De datum van deze dag is:"), (data["list"][max_index]["dt_txt"]))
##print(datum_dag_max_temp)

datum0 = data["list"][0]["dt_txt"]
datum1 = data["list"][1]["dt_txt"]
datum2 = data["list"][2]["dt_txt"]
datum3 = data["list"][3]["dt_txt"]
datum4 = data["list"][4]["dt_txt"]

print(datum0)
print(datum1)
print(datum2)
print(datum3)
print(datum4)

##print(data["list"][0]["dt_txt"])
##print(data["list"][1]["dt_txt"])
##print(data["list"][2]["dt_txt"])
##print(data["list"][3]["dt_txt"])
##print(data["list"][4]["dt_txt"])

print(" ")
