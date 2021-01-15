temp = input()
if temp[0] in ['F']:
    temp = eval(temp[1:])
    c = (temp - 32 ) /1.8
    print("C{:.2f}".format(c))
elif temp[0] in ['C']:
    f = eval(temp[1:]) *1.8 +32
    print("F{:.2f}".format(f))
else:
    print('输入格式错误')
