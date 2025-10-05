numbers = [1,2,3,4,5]
print(type(numbers))

#akeholvek datovy typ moze byt v zozname
combined_list = [1,"Lia", True, 1.5]

#index listu zacina na 0
print(numbers[0:3])

#nahradit hodnotu na indexe 0
#numbers[0] = 10
#print(numbers)
#neda sa pri stringoch
teacher = 'natalia'
#teacher[0] = 'M'
print(teacher)


#operacie s listami
#numbers + [6,7,8]
#numbers = numbers + [6,7,8]
#numbers += [6,7,8]
numbers.extend([6,7,123])
print(numbers)

#funkcie s listami
new_list = [1,3,3]
print(len(new_list))
new_list.append([4,5,6,7])
print(new_list)
print(len(new_list[-1]))

numbers_and_lists=[0, 1, 2, 3, 4, 5, 0, [1, 2], [3, 4, [5]]]
print(numbers_and_lists[-1][-1][0])
numbers_and_lists[-1][-1][0] = 'Lia'
print(numbers_and_lists)

letters = ['n', 'a', 't', 'a', 'l', 'i', 'a']
#letters[0] = 'x'
#pocita kolko krat sa v liste vyskytuje dany prvok
print(letters.count('a'))

num_new = [1,2]
num_new.extend([3,4])
print(num_new)

#vrati index prveho vyskytu prvku
print(letters.index('a'))
letters.insert(0, ['M','L'])
print(letters)

letters.remove('a')
print(letters)

letters.clear()
print(letters)
