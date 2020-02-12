p,m,n = [int(i) for i in input().split()]
studentDict = {}
namelist =[]
def intnum (num):
    if abs(int(num)-num) >= 0.5 :
        return int(num) +1
    else :
        return int(num)

for i in range(p) :
    student = input().split()
    if int(student[1]) >= 200 :
        namelist.append(student[0])
        studentDict[student[0]] = [int(student[1]),-1,-1,0]
for i in range(m) :
    student = input().split()
    try :
        studentDict[student[0]][1] = int(student[1])
    except :
        continue
for i in range(n) :
    student = input().split()
    try :
        studentDict[student[0]][2] = int(student[1])
    except :
        continue

for i in namelist:
    if studentDict[i][1] > studentDict[i][2] :
        studentDict[i][3] = intnum(studentDict[i][1] * 0.4 + studentDict[i][2] * 0.6)
    else :
        studentDict[i][3] = studentDict[i][2]
    if studentDict[i][3] < 60 :
        studentDict.pop(i)
studentlist = sorted(studentDict.items(),key= lambda elem:elem[0])
studentlist.sort(reverse= True,key= lambda elem:elem[1][-1])

for i in studentlist :
    print(i[0],i[1][0],i[1][1],i[1][2],i[1][3])
    