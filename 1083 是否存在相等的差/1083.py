n = int(input())
after = [int(i) for i in input().split()]
chaDict = {}
for i in range(n) :
    cha = abs(after[i] -(i+1))
    try :
        chaDict[cha] += 1
    except :
        chaDict[cha] = 1

chalist = sorted(chaDict.items(),reverse= True,key= lambda elem:elem[0])

for i in chalist :
    if i [1] >= 2 :
        print(i[0],i[1])
