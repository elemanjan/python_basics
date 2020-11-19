def multStr():
    num = int(input("Enter number to multiply string: "))
    st = input("Enter string: ")
    s = ""
    for i in range(0, num, 1):
        s += st
    print(s)


multStr()
