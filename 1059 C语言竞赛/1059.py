import math
n = int(input())
iddict = {input():[i,False] for i in range(n)}
k = int(input())
def isprime (num) :
    for i in range(2,int(math.sqrt(num))+1) :
        if num % i == 0 :
            return False 
    return True

for i in range(k) :
    iDa = input()
    try :
        rank = iddict[iDa][0]
        if iddict[iDa][1] :
            print('{}: Checked'.format(iDa))
        elif rank == 0 :
            print('{}: Mystery Award'.format(iDa))
        elif isprime(rank+1):
            print('{}: Minion'.format(iDa))
        else :
            print('{}: Chocolate'.format(iDa))
        iddict[iDa][1] = True
    except :
        print('{}: Are you kidding?'.format(iDa))

