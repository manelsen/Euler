def reversal(number):
    return(int(str(number)[::-1]))
    
def oddDigits(number):
    for digit in str(number):
        if int(digit) % 2 == 0:
            return(False)
    return(True)
    
reversibles=0
for i in range(1,1000000000):
    if oddDigits(i+reversal(i)):
        if len(str(i)) == len(str(reversal(i))): reversibles+=1
        
print(reversibles)