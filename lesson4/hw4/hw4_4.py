jyl = int(input())

if (jyl % 4 == 0) and (jyl % 100 != 0) or (jyl % 400 == 0):
    print('Високосный')
else:
    print('Обычный')
