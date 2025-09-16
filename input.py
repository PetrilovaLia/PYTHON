#kvader
#input() znamená: "Opýtaj sa používateľa na nejaký údaj".
#int() znamená: "Z toho, čo napíše, sprav celé číslo" 
#lebo inak by to bral ako text).
dlzka = int(input("Zadaj dĺžku: "))
sirka = int(input("Zadaj šírku: "))
vyska = int(input("Zadaj výšku: "))

objem = dlzka * sirka * vyska

#povrch = 2 * (a*b + b*c + a*c)
#3 rôzne dvojice strán, každá sa vyskytuje 2-krát
povrch = 2 * (dlzka*sirka + sirka*vyska + dlzka*vyska)

print("Objem kvádra je:", objem)
print("Povrch kvádra je:", povrch)
