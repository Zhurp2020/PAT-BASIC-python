n,e,d = input().split()
n = int(n)
e = float(e)
d = int(d)
MayEmpty = 0
empty = 0

for i in range(n) :
    house = list(map(float,input().split()))
    house[0] = int(house[0])
    count = 0
    for j in range(1,house[0]+1) :
        if house[j] < e :
            count += 1
    if count > house[0] // 2 :
        if house[0] > d :
            empty += 1   
        else :
            MayEmpty += 1
MayEmpty = (MayEmpty/n) * 100
empty = (empty/n) * 100

print('{:.1f}% {:.1f}%'.format(MayEmpty,empty))        