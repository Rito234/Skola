zaciatok = int(input("Zadaj mi číslo: "))
koniec = int(input("Zadaj mi číslo: "))
vystup = 0
for i in range(zaciatok, koniec + 1):
    vystup = vystup + i #vystup *= i
print(vystup)