n,m = [int(i) for i in input().split()]
itemdict = {}
for i in range(n) :
    item1,item2 = input().split()
    try :
        itemdict[item1].append(item2)
    except :
        itemdict[item1] = [item2]
    try :
        itemdict[item2].append(item1)
    except :
        itemdict[item2] = [item1]    

for i in range(m) :
    flag = False
    cargo = input().split()[1:]
    for item in cargo:
        if item in itemdict :
            for j in itemdict[item] :
                if j in cargo:
                    print('No')
                    flag = True
                    break
        if flag :
            break
    if not flag :
        print('Yes')
