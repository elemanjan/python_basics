arr = [1, 2, 3, 4, 5]
summ = 0
for i in range(0, len(arr), 1):
    arr[i] = arr[i] * arr[i]
    summ += arr[i]
print(summ)
