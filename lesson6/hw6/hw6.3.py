summ = 0

for i in range (0, 1000):
    if ((i % 2 == 0) or (i % 3 == 0)):
        if i % 4 != 0:
        summ += i
print(summ)