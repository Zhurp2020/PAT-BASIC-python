n,m = [int(i) for i in input().split()]
studict = {}
for i in range(n) :
    stu = input().split()
    studict[stu[0]] = int(stu[1])

for i in range(m) :
    require = input().split()
    print('Case {}: {} {}'.format(i+1,require[0],require[1]))
    if require[0] == '1' :
        stulist = []
        for j in studict :
            if j[0] == require[1] :
                stulist.append((j,studict[j]))
        if len(stulist) == 0 :
            print('NA')
            continue
        stulist.sort(key= lambda x:x[0])
        stulist.sort(reverse= True, key= lambda x:x[1])
        for j in stulist :
            print(j[0],j[1])
    elif require[0] == '2' :
        count = score = 0
        for j in studict :
            if j[1:4] == require[1] :
                count += 1
                score += studict[j]
        if count == 0 :
            print('NA')
            continue
        print(count,score)
    elif require[0] == '3' :
        datedict = {}
        for j in studict :
            if j [4:10] == require[1] :
                try:
                    datedict[j[1:4]] += 1
                except :
                    datedict[j[1:4]] = 1
        if len(datedict) == 0:
            print('NA')
            continue
        stulist = sorted(datedict.items(),key= lambda x:x[0])
        stulist.sort(reverse= True, key= lambda x:x[1])
        for j in stulist :
            print(j[0],j)
        
        