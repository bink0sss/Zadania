tablica = {"klucz": "wartosc"}

osoba = {
    "name" :  "Jan",
    "wiek" : "56",
    "miasto" : "Warszawa",
}
print(osoba["miasto"])
print(osoba.get("pesel","Brak Peselu"))
osoba['pesel'] = 881181818
print(osoba)
 

del osoba["miasto"]
print(osoba)
 

if "wiek" in osoba:
    print("Klucz wiek istnieje")

for key, value   in osoba.items():
    print(value)

osoba = {
    "person1" :  {"name":"Jan", "wiek":"46"},
    "person2" : {"name":"Krzys","wiek":"23"}
}
print(osoba.items())