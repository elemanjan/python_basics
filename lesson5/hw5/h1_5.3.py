lst = [2, 3, 4, 5, 6, 7, 8, 9]
lst.reverse()
lst = lst[1:(len(lst))-1]
lst_new = []
for lst in lst:
    lst_new.append(lst * (-10))
