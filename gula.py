import math  # potrebujeme na prácu s pi

r = float(input("Zadaj polomer gule: "))

objem = (4/3) * math.pi * r**3
povrch = 4 * math.pi * r**2

print("Objem gule je:", round(objem, 2))
print("Povrch gule je:", round(povrch, 2))
