m,n,s = list(map(int,input().split()))
nameList = []
awardList = []
for i in range(m) :
    nameList.append(input())

while s <= m:
    i = s-1
    while i <= m-1 :
        if not nameList[i] in awardList :
            awardList.append(nameList[i])
            break
        else :
            i += 1
            s += 1
    s += n

for i in awardList :
    print(i)
if len(awardList) == 0:
    print('Keep going...')