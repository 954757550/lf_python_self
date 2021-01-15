def fab(n):
    if n < 1:
        print("输入有误")
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fab(n - 1) + fab(n - 2)
        
temp = int (input("请输入经过的月数:"))
number = fab(temp)
if number != -1 :
    print("一共有%d个小兔崽子诞生！"% number)
#分治思想
#太慢了，
