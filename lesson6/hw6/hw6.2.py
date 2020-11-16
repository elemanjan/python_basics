a = int(input())
b = int(input())
c = 0
x = 0
lst = []
for i in range(a, b+1, 1):
    if (i % 3) == 0:    
        c +=i
        lst.append(i)
print(c / len(lst))