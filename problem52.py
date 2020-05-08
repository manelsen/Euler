#I'm not proud of it either

x=1
flick=True
while flick:
  if sorted(list(str(x))) == sorted(list(str(x*2))) \
  and sorted(list(str(x))) == sorted(list(str(x*3)))\
  and sorted(list(str(x))) == sorted(list(str(x*4)))\
  and sorted(list(str(x))) == sorted(list(str(x*5)))\
  and sorted(list(str(x))) == sorted(list(str(x*6))):
    print(x)
    flick=False
  x+=1