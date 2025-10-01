#spocitaj parne cisla v intervale
zaciatok = int(input("Zadaj mi číslo: "))
koniec = int(input("Zadaj mi číslo: "))
vystup = 0
for i in range(zaciatok, koniec+1):
    if i % 2 == 0:
        vystup = vystup + i 
print(vystup)