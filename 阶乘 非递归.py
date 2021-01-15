def factorial(n):
    result = n
    for i in range(1,n):
        result *= i
    return result
temp = int(input("请输入一个正整数："))
result = factorial(temp)
print("%d 的阶乘是： %d" % (temp,result))
