a=1
b=1
c=1
def cateto():
	for a in range(1,1000):
		for b in range(1,1000):
			for c in range(1,1000):
				if a**2+b**2==c**2 and a < b and a+b+c == 1000:
					return(a,b,c,a*b*c)
print(cateto())
