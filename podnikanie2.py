# Slovná úloha – Výpočet zisku podnikateľa po zaplatení odvodov a dane
# Podnikateľ dosiahol za rok určitý hrubý zisk. Z tohto zisku musí najprv zaplatiť odvody do poisťovní a následne aj daň z príjmu podľa výšky zisku.
# Pravidlá sú nasledovné:
# Používateľ zadá svoj ročný hrubý zisk v eurách.
# Ak zadá zápornú hodnotu, program vypíše upozornenie:
# Ak je hodnota kladná, najprv sa vypočítajú odvody:
# 33,15 % z hrubého zisku
# (táto suma predstavuje sociálne a zdravotné poistenie)
# Potom sa vypočíta zdaniteľný zisk = hrubý zisk – odvody.
# Daň sa určí podľa výšky zdaniteľného zisku:
# ak je zdaniteľný zisk do 49 790 €, daň je 15 %
# ak je vyšší, daň je 21 %

# Program nakoniec vypíše:
# výšku odvodov
# výšku dane
# a čistý zisk po zdanení a odvodoch (hrubý zisk – odvody – daň)

# Postup riešenia:

# Vstupné údaje:
# Načítam od používateľa hrubý zisk pomocou input() a prevediem ho na číslo typu float.

# Kontrola vstupu:
# Ak je hodnota záporná, vypíšem upozornenie a program skončí.

# Výpočet odvodov:
# Vypočítam 33,15 % z hrubého zisku:

# Výpočet dane:
# Použijem vetvenie:

# ak je zdaniteľný zisk do 49 790 €, použijem 15 %,

# inak 21 %.

# Čistý zisk:
# Od hrubého zisku odpočítam odvody aj daň.

# Výstup:
# Vypíšem prehľadne všetky výsledky, zaokrúhlené na dve desatinné miesta.

hruby_zisk = float(input("Zadaj ročný hrubý zisk: "))

if hruby_zisk < 0:
    print("Pozor, zadali ste záporný zisk.")
else:
    odvody = hruby_zisk * 0.3315
    zdanitelny = hruby_zisk - odvody

    if zdanitelny <= 49790:
        dan = zdanitelny * 0.15
    else:
        dan = zdanitelny * 0.21

    cisty_zisk = hruby_zisk - odvody - dan

    print("----- Výsledok -----")
    print("Hrubý zisk:", round(hruby_zisk, 2), "eur")
    print("Odvody:", round(odvody, 2), "eur")
    print("Daň:", round(dan, 2), "eur")
    print("Čistý zisk po odvodoch a dani:", round(cisty_zisk, 2), "eur")
