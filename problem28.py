def side(number):
  summa=0
  for i in range(0,4):
    a=number-1
    b=a*i
    summa = summa + number**2-b
  return(summa)

def diagonals(number):
  total=1
  for i in range(3,number+1,2):
    total+=side(i)
  return(total)

print(diagonals(1001))