from math import *
n = int(input())
prime = [] 
for i in range(2,n+1):
        prime.append(i)
count = 0
def isprime(num) :
    for i in range(2,int(sqrt(num))+1) :
        if num % i == 0 :
            return False 
    return True

for i in prime :
   if isprime(i)  :
        for j in range(2*i,n+1,i) :
            if i * j in prime :
                prime.remove(i*j)
for i in range(len(prime)-1) :
    if prime[i+1] - prime[i] == 2 :
        count = count + 1

print(count)





#def prime(n,result):
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
 
#a = int(input())
#result = []
#prime(a,result)
#num = 0
#for i in range(len(result)-1):
#    if (result[i+1]-result[i]==2):
#        num+=1

# 让我们定义d​n为：d​n=p​n+1−pn，其中pi是第i个素数。显然有d1=1，且对于n>1有dn是偶数。
# “素数对猜想”认为“存在无穷多对相邻且差为2的素数”。
# (<105)，请计算不超过N的满足猜想的素数对的个数。

 