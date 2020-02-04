n,m = list(map(int,input().split()))
scores = input().split()
ans = input().split()
ProDict = {i:[int(scores[i]),ans[i]] for i in range(m)}
StuScore = [0 for i in range(n)]

for i in range(n) :
    AStu = input().split()
    for j in range(m) :
        if AStu[j] == ProDict[j][1] :
            StuScore[i] += ProDict[j][0]
            
for i in StuScore :
    print(i)

