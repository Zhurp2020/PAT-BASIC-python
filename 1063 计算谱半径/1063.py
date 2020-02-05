import math
n = int(input())
MoList = []
for i in range(n) :
    aCom = list(map(int,input().split()))
    Mo = math.sqrt(aCom[0]**2 + aCom[1]**2)
    MoList.append(Mo)

print('{:.2f}'.format(max(MoList)))
