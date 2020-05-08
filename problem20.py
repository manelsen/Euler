def factorial(number):
  total=1
  for i in range(1,number):
    total *= i
  return(total)

a = str(factorial(100))
sum=0
for digit in a:
  sum += int(digit)

print(sum)