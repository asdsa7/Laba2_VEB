def backwards (x):
	lower = x < 0
	if lower:
		x *= -1
	y = 0
	while x > 0:
		z = x % 10
		y = y * 10 + z
		x = x // 10
	if lower:
		y *= -1
	return y 


print (backwards(int(input("Введите число: "))))