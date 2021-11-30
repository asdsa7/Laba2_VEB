def getLists (lst):
	x2 = []
	x3 = []
	x5 = []
	for i in lst:
		if i % 2 == 0: x2.append(i)
		if i % 3 == 0: x3.append(i)
		if i % 5 == 0: x5.append(i)
	return [x2, x3, x5]

x = getLists([int(i) for i in input('Введите значения: ').split()])
print(x)
