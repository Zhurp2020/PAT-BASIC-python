n,m = [int(i) for i in input().split()]
items = input().split()
ctstu,ctitem = 0,0

for i in range(n) :
    student = input().split()
    ilegal = []
    for j in student[2:] :
        if j in items :
            ilegal.append(j)
            ctitem += 1
    if len(ilegal) > 0 :
        print('{}: {}'.format(student[0],' '.join(ilegal)))
        ctstu += 1
        
print(ctstu,ctitem)