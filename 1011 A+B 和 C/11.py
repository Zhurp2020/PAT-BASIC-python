n = int(input())
reslist = []
for i in range(n) :
    a,b,c = input().split()
    if int(a) +int(b) > int(c) :
        reslist.append('true') 
    else :
        reslist.append('false') 

for i in range(n) :
    print('Case #',i+1,': ',reslist[i],sep = '')


# 给定区间 [−231,231] 内的 3 个整数 A、B 和 C，请判断 A+B 是否大于 C。