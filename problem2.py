f = [0, 1]
for n in range(1,100):
	if (f[n]+f[n-1]) >= 4000000:
		break
	else:
		f.append(f[n]+f[n-1])
print(sum([x for x in f if x % 2 == 0]))
