def euler29():
  answer=[]
  for i in range(2,101):
    for j in range(2,101):
      if i**j not in answer: answer.append(i**j)
  print(len(answer))

euler29()