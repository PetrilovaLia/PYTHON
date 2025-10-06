# Podmienky if, elif, else
# Program vykoná určitý blok kódu, ak je splnená podmienka
# Syntax: 
# if podmienka: 
#   blok_kódu
# elif 
#   iná_podmienka:

if False:
    print('Je pravda')
else:
    print('Nie je pravda')    


is_student = False

if is_student == True:
    print('Je student')
else:
    print('Nie je študent')

# reťazenie podmienok
is_student = False
is_teacher = False

if is_student == True:
    print('Je student')
elif is_teacher == True:
    print('Je učiteľ')
else:
    print('Nie je študent ani učiteľ')

# Každé číslo, ktoré nie je 0 má hodnotu True (aj záporné)
if 1:
    print('Je pravda')
else:
    print('Nie je pravda')

if 0:
    print('Je pravda')
else:
    print('Nie je pravda')

if -135:
    print('Je pravda')
else:
    print('Nie je pravda')

# porovnanie listov
list_1 = [1,2,3]
list_2 = [1,2,3]

if list_1 == list_2:
    print('Listy sú rovnaké')
else:
    print('Listy nie sú rovnaké')

# porovnanie stringov a uloženie do premennej
is_student = True
if is_student == True:
    is_student_status = 'Je student'
else:
    is_student_status = 'Nie je študent'
print(is_student_status)

#
