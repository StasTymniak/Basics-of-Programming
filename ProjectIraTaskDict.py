def saveFile(my_dict):
	string = ''
	for country in my_dict:
		string += country + '-'
		for i in range(len(my_dict[country])):
			string += my_dict[country][i] + ','
		string = string[:-1]
		string += '\n'

	text_file = open("text.txt", "w")
	n = text_file.write(string)
	text_file.close()
	print('File saved')
	main(my_dict)


def addCountry(my_dict):
	country = input("Enter country : ")
	city = []
	while True:
		elem = input('Enter city (stop) : ')
		if not elem == 'stop':
			city.append(elem.title())
		else:
			break
		
	my_dict[country.title()] = city
	return my_dict


def deleteCountry(my_dict):
	country = input('Enter country which you want delete: ')
	my_dict.pop(country.title())
	return my_dict
	

def outputCountry(my_dict):
	first = input('Enter first letter: ')
	for country in my_dict:
		if country[0] == first.upper():
			print(country, '-', ','.join(my_dict[country]))
	main(my_dict)


def printDict(my_dict):
	for country in my_dict:
		print(country, '-', ', '.join(my_dict[country]))
	main(my_dict)


def printCapital(my_dict):
	for country in my_dict:
		print(my_dict[country][0], 'is capital of', country)
	main(my_dict)


def findCountry(my_dict):
	city = input('Enter city : ')
	for country in my_dict:
		if city.title() in my_dict[country]:
			print(city.title(), 'is located in', country)
	main(my_dict)


def editDict(my_dict):
	country = input('Enter country which you want edit : ')
	choose = input('You want edit capital or city: ')
	choose = choose.lower()
	if choose == 'capital':
		print('Capital now : ', my_dict[country.title()][0])
		newCapital = input('Enter new capital : ')
		my_dict[country.title()][0] = newCapital.title()
	elif choose == 'city':
		for i in range(1,len(my_dict[country.title()])):
			print(i, '.', my_dict[country.title()][i])
		indexCity = int(input('Enter number city : '))
		newCity = input('Enter new city : ')
		my_dict[country.title()][indexCity] = newCity.title()
	main(my_dict)
			

def sortDict(my_dict):
	arr = []
	for i in my_dict:
		arr.append(i)
	arr = sorted(arr)
	for country in arr:
		print(country, '-', ', '.join(my_dict[country]))
	main(my_dict)


def createArr(my_dict):
	capital = []
	city = []
	for i in my_dict:
		capital.append(my_dict[i][0])
		for j in range(1,len(my_dict[i])):
			city.append(my_dict[i][j])
	print('Capital : ', ', '.join(capital))
	print('City : ', ', '.join(city))
	main(my_dict)

f = open("text.txt", "r+")
f1 = f.readlines()
arr = []
my_dict = dict()
key = [',','\n','.','!','?','/','\t',' ']

for x in f1:
	arr.append(x)
for i in arr:
	string = []
	i_list = list(i.split('-'))
	city = list(i_list[1].split(','))

	for word in city:
		word_list = list(word)
		for i in range(len(key)):
			if key[i] in word_list:
				word_list.remove(key[i])
		string.append(''.join(word_list))

	my_dict[i_list[0]] = string


def main(my_dict):
	op = input('Enter operation : ')
	op = op.lower()
	if op == 'del':
		my_dict = deleteCountry(my_dict)
		main(my_dict)
	elif op == 'print':
		printDict(my_dict)
	elif op == 'first':
		outputCountry(my_dict)
	elif op == 'save':
		saveFile(my_dict)
	elif op == 'add':
		my_dict = addCountry(my_dict)
		main(my_dict)
	elif op == 'capital':
		printCapital(my_dict)
	elif op == 'find':
		findCountry(my_dict)
	elif op == 'edit':
		editDict(my_dict)
	elif op == 'sort':
		sortDict(my_dict)
	elif op == 'create':
		createArr(my_dict)
	elif op == 'help':
		print('''-Save dictionary enter : save
-Add country enter : add
-Delete country enter : del
-Print dictionary enter : print
-Print country first letter enter : first
-Find country by city enter : find
-Print capital enter : capital 
-Edit dictionary enter : edit
-Sort dictionary enter : sort
-Create array with capital and city enter: create''')
		main(my_dict)
	else:
		print('You enter wrong operation')
		main(my_dict)

main(my_dict)
