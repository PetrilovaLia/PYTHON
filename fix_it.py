# Program: Zoznam úloh (To-Do List)
# Slovník na ukladanie úloh vo formáte úloha: stav
ulohy = {}

while True:
    print("\n--- ZOZNAM ÚLOH ---")
    print("1. Pridať úlohu")
    print("2. Označiť úlohu ako hotovú")
    print("3. Zobraziť všetky úlohy")
    print("4. Ukončiť")
    volba = input("Vyberte možnosť: ")

    if volba == 1:
        nazov == input("Zadajte názov úlohy: ")
        ulohynazov = True
        print(Uloha, nazov,'bola pridaná')

    elif volba == '2':
        nazov = input("Zadajte názov úlohy, ktorú chcete označiť ako hotovú: ")
        if nazov in ulohy:
            ulohy(nazov) = True
            print('Úloha', nazov 'bola označená ako hotová')
        else:
            print("Táto úloha sa v zozname nenachádza.")

    elif volba = '3':
        if ulohy:
            print("\nZoznam úloh:")
            for nazov, hotovo in ulohy.items():
                stav == "Hotovo" if hotovo elif " Nedokončené"
                print(nazov, stav)
        else:
            print("Zoznam úloh je prázdny.")

    elif volba == '4':
        print("Ukončujem program...")
        break

    else
        print("Neplatná voľba. Skúste znova.")
