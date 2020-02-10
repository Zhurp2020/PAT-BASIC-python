import re
n,m = [int(i) for i in input().split()]
prodict = {}
ans = re.compile(r'\(.+?\)')
scorelist = []
wrongdict = {i+1:{} for i in range(m)}

for i in range(m) :
    problem = input().split()
    prodict[i+1] = [float(problem[0]),problem[3:]]
for i in range(n) :
    score = 0.0 
    stu = [j.rstrip(')').split()[1:] for j in ans.findall(input())] 
    for j in range(m) :
        pright = True
        if stu[j] == prodict[j+1][1] :
            score += prodict[j+1][0]
            pright = False
            continue
        else :
            for k in stu[j] :
                if not k in prodict[j+1][1] :
                    pright = False
                    try :
                        wrongdict[j+1][k] += 1 
                    except :
                        wrongdict[j+1][k] = 1  
        if pright :
            score += prodict[j+1][0]/2
        for k in prodict[j+1][1] :
            if not k in stu[j] :
                try :
                    wrongdict[j+1][k] += 1 
                except :
                    wrongdict[j+1][k] = 1 
    scorelist.append(score)
\

for i in scorelist :
        print(i)
try: 
    maxwrong = max([max(wrongdict[i+1].values()) for i in range(m)]) 
except :
    print('Too simple')
   
for i in range(m) :
    anslist= []
    for j in wrongdict[i+1] :
        if wrongdict[i+1][j] == maxwrong :
            anslist.append((j,i+1))
    anslist.sort()
    for j in anslist:
        print('{} {}-{}'.format(maxwrong,j[1],j[0]))
        

