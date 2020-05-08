def collatz(number):
  terms=1
  link=number
  while link != 1:
    if link % 2 == 0: link = link//2
    else: link = 3 * link + 1
    terms+=1
  return(terms)

def euler(number):
  collatzes=[]
  for i in range(1,number+1):
    collatzes.append([i,collatz(i)])
  return(collatzes)

def max_euler(listOfNumbers):
  maxIndex=0
  maxValue=0
  for i in listOfNumbers:
    if i[1]>maxValue:
      maxValue=i[1]
      maxIndex=i[0]
  return(maxIndex,maxValue)

print(max_euler(euler(1000000)))