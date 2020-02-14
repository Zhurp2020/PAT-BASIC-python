n = int(input())
schooldict = {}
for i in range(n) :
    number,score,name = input().split()
    name = name.lower()
    try :
        schooldict[name][1] += 1
    except :
        schooldict[name] = [0,1]
    if number[0] == 'B' :
        schooldict[name][0] += int(score)/1.5
    elif number[0] == 'A' :
        schooldict[name][0] += int(score)
    elif  number[0] == 'T':
        schooldict[name][0] += int(score) * 1.5

for i in schooldict :
    schooldict[i][0] = int(schooldict[i][0])
schoolList = sorted(schooldict.items(),key= lambda x:x[0])
schoolList.sort(key= lambda x:x[1][1])
schoolList.sort(reverse=True,key= lambda x:x[1][0])
amount = len(schoolList)

print(amount)
count = 1
print(count,schoolList[0][0],schoolList[0][1][0],schoolList[0][1][1])
for i in range(1,amount) :
    if schoolList[i][1][0] != schoolList[i-1][1][0] :
        count = 1 + i
    print(count,schoolList[i][0],schoolList[i][1][0],schoolList[i][1][1])
    
