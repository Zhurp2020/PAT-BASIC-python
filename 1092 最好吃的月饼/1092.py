n,m = [int(i) for i in input().split()]
mkdict = {i:0 for i in range(1,n+1)}
for i in range(m) :
    number = [int(i) for i in input().split()]
    for j in range(1,n+1) :
        mkdict[j] += number[j-1]

maxmk = max(mkdict.values())

print(maxmk)
maxlist = []
for i in mkdict:
    if mkdict[i] == maxmk:
        maxlist.append(i)
print(' '.join([str(i)for i in maxlist]))
