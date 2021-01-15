sum1 = sum2 = sum3 = 0

def sum11():
    global sum1 ,sum2,sum3 # 用global 使得函数内部可以修改全局变量，，，完全可以把sum1 = 0放在函数内，我就是用用global
    for i in range(0,11):
        sum1 += i

    for i in range(20,31):
        sum2 += i

    for i in range(35,46):
        sum3 += i
    print(sum1,sum2,sum3)

def sum22():
    print(sum(range(0,11)))
    print(sum(range(20,31)))
    print(sum(range(35,46)))
sum11()
sum22()
