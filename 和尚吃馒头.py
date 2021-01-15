sum1 = 100
sum2 = 100
num_small = 0
num_big = 100
while(  sum1 != 0 ):
    sum1 = sum1 - 3 * num_big
    if(sum1 < 0):#说明大和尚多了，馒头不够分，需要大和尚减少
        num_big -= 1
        num_small += 1
        sum1 = 100
    sum1 = sum1 - 3 * num_big - num_small / 3
print('大和尚数量为:%d,小和尚数量为:%d'%(num_big,num_small))
        
    
