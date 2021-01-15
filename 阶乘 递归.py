def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
number = int (input("请输入一个正整数："))
result = factorial(number)
print("%d 的阶乘是 %d"%( number,result))
print("{:d}".format(result))
print("{:.3f}".format(result)) #format形式输出保留三位小数
