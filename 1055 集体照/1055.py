n,k = list(map(int,input().split()))
mandict = {}
for i in range(n) :
    man = input().split()
    mandict[man[0]] = int(man[1])

man4row = int(n/k)
manlist = sorted(mandict.items(),key= lambda elem:elem[0])
manlist.sort(key= lambda elem:elem[1],reverse= True)
row0 = manlist[:man4row+n%k]
row0name = [0 for i in row0]
m = int(len(row0)/2)
row0name[m] = row0[0][0]
r0mleft = m-1
r0mrit = m+1

for i in range(man4row+n%k-1) :
    if i % 2 == 0 :
        row0name[r0mleft] = row0[i+1][0]
        r0mleft -= 1
    else :
        row0name[r0mrit] = row0[i+1][0]
        r0mrit += 1
print(' '.join(row0name))
for i in range(0,k-1) :
    arow = manlist[man4row+n%k+i*man4row:man4row+n%k+(i+1)*man4row]
    m = int(man4row/2)
    arowname = [0 for j in arow]
    arowname[m] = arow[0][0]
    mleft = m-1
    mrit = m+1
    for j in range(man4row-1) :
        if j % 2 == 0 :
            arowname[mleft] = arow[j+1][0]
            mleft -= 1
        else :
            arowname[mrit] = arow[j+1][0]
            mrit += 1
    print(' '.join(arowname))


