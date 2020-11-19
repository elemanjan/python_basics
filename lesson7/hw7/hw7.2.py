def findCoord():
    x = []
    y = []
    z = []
    sum = 0
    for i in range(0, 5, 1):
        x.append(int(input()))
        y.append(int(input()))
    sumx = 0
    sumy = 0
    for i in range(0, len(x), 1):
        sumx += x[i]
    z.append(sumx)
    for i in range(0, len(y)):
        sumy += y[i]
    z.append(sumy)
    print(z)


findCoord()
