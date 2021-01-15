a = input()
if a[-1] in ['F','f']:
    a = float(a[0:-1])
    C = (a - 32)/1.8
    print("{:.2f}C".format(C))
elif a[-1] in ['C','c']:
    a = float(a[0:-1])
    F = 1.8 * a + 32
    print("{:.2f}F".format(F))
else:
    print("输入格式错误")
