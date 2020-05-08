def checkPower(number,power):
  digits=str(number)
  summa=0
  for digit in range(len(digits)):
    summa+=int(digits[digit])**power
  return(summa)

total=0
for i in range(2,10000000):
  if checkPower(i,5)==i:
    print(i)
    total+=i
print("Total:",total)