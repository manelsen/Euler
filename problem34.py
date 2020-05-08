def euler34(number):
  answer=[]
  for i in range(3,number):
    digits=str(i)
    summa=0
    for digit in digits:
      summa+=factorial(int(digit))
    if summa == i:
      answer.append(i)
  return(sum(answer))

def factorial(number):
  summa=1
  for i in range(1,number+1):
    summa*=i
  return(summa)

print(euler34(9999999))