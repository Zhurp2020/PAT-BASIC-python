n = int(input())
IDList = []
for i in range(n) :
    a,b = input().split()
    IDList.append(a)
    IDList.append(b)
m = int(input())
manList = set(input().split())

for i in range(0,2*n,2) :
    if IDList[i] in manList and IDList[i+1] in manList :
        manList.remove(IDList[i])
        manList.remove(IDList[i+1])
manList = list(manList)       
manList.sort()

print(len(manList))
if len(manList) != 0  :
    print(' '.join(manList))