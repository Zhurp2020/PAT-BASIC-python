n,l,h = [int(i) for i in input().split()]
scoredict = {}
for i in range(int(n)) :
    student = [int(i) for i in input().split()]
    scoredict[student[0]] = [student[1],student[2]]
class1 = []
class2 = []
class3 = []
class4 = []
def sortclass (listin) :
    listin.sort(key= lambda elem : (-(elem[1][0] + elem[1][1]),-elem [1][0],int(elem [0])))
    #listin.sort(key= lambda elem : ,reverse= True)
    #listin.sort(key= lambda elem : ,reverse= True )
    return listin

for i in scoredict :
    if scoredict[i][0] >= h and scoredict[i][1] >= h :
        class1.append([i,scoredict[i]])
    elif scoredict[i][0] >= h and l <= scoredict[i][1] < h :
        class2.append([i,scoredict[i]])
    elif l <= scoredict[i][0] < h and l <= scoredict[i][1] < h and scoredict[i][0] >= scoredict[i][1]:
        class3.append([i,scoredict[i]])
    elif l <= scoredict[i][0] and l <= scoredict[i][1] :
        class4.append([i,scoredict[i]])
class1 = sortclass(class1)
class2 = sortclass(class2)
class3 = sortclass(class3)
class4 = sortclass(class4)

print(len(class1) + len(class2) + len(class3) + len(class4))
for i in class1 :
    print(i[0],i[1][0],i[1][1])
for i in class2 :
    print(i[0],i[1][0],i[1][1])
for i in class3 :
    print(i[0],i[1][0],i[1][1])
for i in class4 :
    print(i[0],i[1][0],i[1][1])

