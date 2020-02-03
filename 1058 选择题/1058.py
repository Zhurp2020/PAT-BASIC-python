import re
n,m = list(map(int,input().split()))
prodict = {}
ans = re.compile(r'\(.+?\)')
scorelist = []

for i in range(m) :
    problem = input().split()
    prodict[i+1] = [int(problem[0]),problem[3:],0]
for i in range(n) :
    score = 0 
    stu = [j.rstrip(')').split()[1:] for j in ans.findall(input())] 
    for j in range(m) :
        if stu[j] == prodict[j+1][1] :
            score += prodict[j+1][0]
        else :
            prodict[j+1][2] += 1
    scorelist.append(score)
maxwrong = max(prodict.items(),key= lambda elem:elem[1][2])[1][2]

for i in scorelist :
    print(i)
if maxwrong == 0 :
    print('Too simple')
else :
    print(maxwrong,end=' ')
    res = ''
    for i in range(m) :
        if prodict[i+1][2] == maxwrong :
            res += str(i+1) + ' '
    print(res.rstrip())

    
