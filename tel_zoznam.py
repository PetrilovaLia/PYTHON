#slovník na ukladanie kontaktov meno:čislo
kontakty = {}

#nekonečný cyklus, kým nezvolím "4"
while True:
    print("\n--- Telefónny zoznam ---")
    print("1. Pridať kontakt")
    print("2. Vyhľadať kontakt")
    print("3. Zobraziť všetky kontakty")
    print("4. Ukončiť")
    volba = input("Vyberte možnosť: ")

    if volba == "1":
        meno = input("Zadajte meno kontaktu: ")
        cislo = input("Zadajte telefónne číslo: ")
        kontakty[meno] = cislo
        print("Kontakt bol pridaný.")

#kontakty.items() vracia dvojice (meno, cislo)
    elif volba == "2":
        if kontakty:
            print("Všetky kontakty:")
            for meno, cislo in kontakty.items():
                print(f"{meno}: {cislo}")
        else:
            print("Zoznam kontaktov je prázdny.")
            
#Program sa pokúsi nájsť číslo pomocou kontakty.get(meno)
#get vráti číslo, ak meno existuje, alebo None, ak neexistuje (vtedy vypíše „Kontakt sa nenašiel“)
    elif volba == "3":
        meno = input("Zadajte meno kontaktu: ")
        cislo = kontakty.get(meno)
        if cislo:
            print(f"{meno} - {cislo}")
        else:
            print("Kontakt sa nenašiel.")

    
    elif volba == "4":
        print("Ukončujem program...")
        break

    else:
        print("Neplatná voľba. Skúste znova.")

meno = 'Alex'
vek = 18

print(meno + ' : ' + str(vek))
print(meno, ':', vek)
print(f'{meno} : {vek}')
print('%s : %s ' % (meno, vek))
print('{} : {}' .format(meno,vek))
