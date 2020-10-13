import math
a,b = input().split()
def isprime(num) :
    for i in range(2,int(math.sqrt(num))+1) :
        if num % i == 0 :
            return False 
    return True
primelist = []
nums = (i for i in range(2,105000))
res = ''
count = 0

for i in nums :
    if isprime(i) :
        count = count+1
        if count == int(a) :
            pm = i
        if count == int(b) :
            pn = i
            break
for i in range (pm,pn + 1) :
    if isprime(i) :
        primelist.append(i)

for i in range(len(primelist) // 10) :
    for j in range(i*10,i*10+10) :
        res = res + str(primelist[j]) + ' '
    print(res.rstrip())
    res = ''
if len(primelist) % 10 != 0:
    for i in range((len(primelist) // 10)*10,len(primelist)) :
        res = res + str(primelist[i]) + ' '
    print(res.rstrip())



# def prime(n,result):
#    flag = [1]*(n+2)
#    p=2
#    while(p<=n):
#        result.append(p)
#        for i in range(2*p,n+1,p):
#            flag[i] = 0
#        while 1:
#            p += 1
#            if(flag[p]==1):
#                break
#a = input().split()
#result = []
#prime(200000,result)
#final = result[int(a[0])-1:int(a[1])]
#if len(final)==1:
#    print(final[0])
#else:
#    for i in range(len(final)-1):
#        if (i+1)%10==0:
#            print(final[i]) 
#        else:
#            print(final[i],end=" ")
#    if (i+2)%10==0:
#        print(final[i+1]) 
#   else:
#        print(final[i+1],end="")



# 令 Pi表示第 i 个素数。现任给两个正整数 M≤N≤104，
# 请输出 PM到 PN的所有素数。