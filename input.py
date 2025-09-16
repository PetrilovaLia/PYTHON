#kvader
dlzka = int(input("Zadaj dĺžku: "))
sirka = int(input("Zadaj šírku: "))
vyska = int(input("Zadaj výšku: "))

objem = dlzka * sirka * vyska
povrch = 2 * (dlzka*sirka + sirka*vyska + dlzka*vyska)

print("Objem kvádra je:", objem)
print("Povrch kvádra je:", povrch)
