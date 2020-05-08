old_fibo=2
fibo=3
index=4
while len(str(fibo))<1000:
  old_fibo,fibo=fibo,old_fibo+fibo
  index+=1
print(index)