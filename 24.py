a,b = input().split('E')
b = int(b)
temp = a.split('.')

if b < 0 :    
    c = '0.' + '0' * (-b-1) + temp[0][1:] + temp[1]
elif b > 0 :
    if len(temp[1]) > b :
        c = temp[0][1:] + temp[1][0:b] + '.' + temp[1][b:]
    elif len(temp[1]) == b :
        c = temp[0][1:] + temp[1][0:b]
    else :
        c = temp[0][1:] + temp[1] + '0' * (b-len(temp[1]))
else :
    c = a
if temp[0][0] == '-' :
    print('-' + c)
else :
    print(c)



# 科学计数法是科学家用来表示很大或很小的数字的一种方便的方法，
# 其满足正则表达式 [+-][1-9].[0-9]+E[+-][0-9]+，
# 即数字的整数部分只有 1 位，小数部分至少有 1 位，
# 该数字及其指数部分的正负号即使对正数也必定明确给出。
# 现以科学计数法的格式给出实数 A，
# SS请编写程序按普通数字表示法输出 A，并保证所有有效位都被保留。