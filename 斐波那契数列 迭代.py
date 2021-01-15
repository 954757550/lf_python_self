def fab(n):
    n1 = 1
    n2 = 1
    n3 = 1
    if n < 1:
        print("输入有误")
        return -1
    while (n - 2 ) > 0 :
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        n -= 1
    return n3

temp = int(input("请输入所经过的月数:"))
number = fab(temp)
if number != -1:
    print("共有%d对小兔崽子诞生"% number)
               
