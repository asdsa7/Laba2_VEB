def polindrom (x):
	lower = x < 0
	if lower:
		x *= -1
	y = x
	z = 0
	while x > 0:
		w = x % 10
		z = z * 10 + w
		x = x // 10
	return z == y


print(polindrom(int(input("Введите число: "))))