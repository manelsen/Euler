y = 20
x = 1

while True:
	if x % y == 0:
		y -= 1
		if y == 2:
			break
	else:
		y = 20
		x += 1
print(x)
