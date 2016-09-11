print(max([i * j for i in range(1000,10000) for j in range(1000,10000) if str(i*j) == str(i*j)[::-1]]))
