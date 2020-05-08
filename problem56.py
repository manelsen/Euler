max = 0
for i in range(1,100):
  for j in range(1,100):
    summa=0
    for digit in str(i**j):
      summa+=int(digit)
    if summa > max:
      max = summa
print(max)