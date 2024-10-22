napis = "Witaj w Pythonie"
print(napis.upper())

print(napis.index("W"))

print(f"{napis}")

owoce = ["jabłko", "gruszka", "banan"]
owoce.append("pomarańcza")
print(owoce[0])

owoce.remove("gruszka")
print(owoce)

owoc = owoce.pop(0)
print(owoc)
print(owoce)

len(owoce)
print(owoce)

owoce.sort(reverse = True)
print(owoce)

index = owoce.index("pomarańcza")
print(index)

#krotki /tuple

współrzędne = (10,(20,30),"WITAJ") # x,y,z
print(współrzędne[2])
print(współrzędne)

a,*b = współrzędne
print(b)