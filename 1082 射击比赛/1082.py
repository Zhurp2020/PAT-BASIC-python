import math
n = int(input())
idDict = {}
for i in range(n) :
    Id,x,y = input().split()
    dist = math.sqrt(int(x)**2 + int(y) ** 2)
    idDict[Id] = dist

maxid = max(idDict.items(),key= lambda elem:elem[1])
minid = min(idDict.items(),key= lambda elem:elem[1])

print(minid[0],maxid[0])