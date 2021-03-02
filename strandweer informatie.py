msg = "Welkom bij strandweer informatie"
print(msg)

##lijst_met_plaatsnamen = [Scheveningen0, Katwijk1, Zandvoort2, Noordwijk3]
##print(lijst_met_plaatsnamen)
##indices = [0, 2]
##selected_elements = []
##Initialize result list

##for index in indices:
##    selected_elements.append(a_list[index])
##Add chosen items to result list

##print(selected_elements)

plaatsnaam = input("Beste gebruiker kies een badplaats: ")

print("U heeft gekozen voor de badplaats: " + plaatsnaam)

## link = "https://api.openweathermap.org/data/2.5/forecast/?q=scheveningen&units=metric&cnt=5&appid=a7f9e1a6b04a8b787e857547840c3a36"
import requests
import json

q = plaatsnaam
## q = "scheveningen"
appid = "a7f9e1a6b04a8b787e857547840c3a36"
url = (
    "https://api.openweathermap.org/data/2.5/forecast?q=%s&appid=%s&units=metric&cnt=5"
    % (
        q,
        appid,
    )
)

##url = "https://api.openweathermap.org/data/2.5/forecast/?q=london&units=metric&cnt=5&appid=a7f9e1a6b04a8b787e857547840c3a36"
##url = "https://api.openweathermap.org/data/2.5/forecast/?q=scheveningen&units=metric&cnt=5&appid=a7f9e1a6b04a8b787e857547840c3a36"

response = requests.get(url)
data = json.loads(response.text)

##print(data["list"][0]["main"]["temp"])
##print(data["list"][1]["main"]["temp"])
##print(data["list"][2]["main"]["temp"])
##print(data["list"][3]["main"]["temp"])
##print(data["list"][4]["main"]["temp"])
##print(data)

##temp0 = data["list"][0]["main"]["temp"]
##temp1 = data["list"][1]["main"]["temp"]
##temp2 = data["list"][2]["main"]["temp"]
##temp3 = data["list"][3]["main"]["temp"]
##temp4 = data["list"][4]["main"]["temp"]

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
