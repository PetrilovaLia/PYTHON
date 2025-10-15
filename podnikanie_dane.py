# Napíš program, ktorý vypočíta daň z ročného príjmu fyzickej osoby podľa nasledujúcich pravidiel:
# Používateľ zadá svoj ročný príjem (v eurách).

# Ak zadá záporné číslo, program vypíše upozornenie: Pozor, zadali ste záporný príjem.
# Ak je príjem menší ako 48 441,43 €, daň sa počíta ako 19 % z celého príjmu.

# Ak je príjem vyšší alebo rovný 48 441,43 €, daň sa vypočíta nasledovne:
# z prvých 48 441,43 € sa platí 19 %,
# zo zvyšku príjmu (teda z toho, čo presahuje 48 441,43 €) sa platí 25 %.

# Program nakoniec vypíše sumu dane zaokrúhlenú na dve desatinné miesta, napríklad:
# Daň z príjmu je: 8234.17 eur

# Postup riešenia úlohy
# používateľ zadá svoj ročný príjem,
# podľa výšky príjmu sa vypočíta daň podľa dvoch sadzieb,
# výsledok sa vypíše.
# Treba ošetriť aj prípad, keď je príjem záporný.

# Vstup od používateľa
# Potrebujem, aby program vedel, aký je ročný príjem.
# Použijem funkciu input() a prepočítam textový vstup na číslo typu float, aby som mohla pracovať s desatinnými číslami:

prijem = float(input("Zadaj ročný príjem: "))

# Kontrola vstupu
# Zo zadania viem, že ak je príjem záporný, treba vypísať upozornenie.
# Na to použijem podmienku if:
if prijem < 0:
    print("Pozor, zadali ste záporný príjem.")

# Ak je podmienka splnená, program už ďalej nič nepočíta.
# Rozdelenie výpočtu podľa výšky príjmu
# Ak príjem nie je záporný, musím zistiť, do ktorej daňovej sadzby patrí.
# Preto použijem vetvenie if ... else:

# Ak je príjem menší ako 48 441,43 €, daň je 19 % z príjmu.

# Inak je daň zložená z dvoch častí.
else:
    if prijem < 48441.43:
        dan = prijem * 0.19
    else:
        dan = 48441.43 * 0.19 + (prijem - 48441.43) * 0.25

# Výstup výsledku
# Nakoniec treba vypísať výslednú daň.
# Zo zadania viem, že sa má zaokrúhliť na dve desatinné miesta – použijem funkciu round():
print("Daň z príjmu je:", round(dan, 2), "eur")

# Testovanie programu
# Otestujem program s rôznymi vstupmi:
# napr. prijem = -1000 → upozornenie,
# prijem = 20000 → 19 % dane,
# prijem = 60000 → kombinovaná daň (19 % + 25 %).

