y = 20
x = 20

while True:
	if x % y == 0:
		y -= 1
		if y == 2:
			break
	else:
		y = 20
		x += 20
print(x)
