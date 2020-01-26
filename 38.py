n = int(input())
scores = list(map(int,input().split()))
ks = list(map(int,input().split()))
scoresdict = {i:0 for i in scores}
res = ''

for i in scores :
    scoresdict[i] += 1

for i in range(ks[0]) :
    if ks[i+1] in scoresdict :
        res += str(scoresdict[ks[i+1]]) + ' '
    else :
        res  += '0 '
print(res.rstrip())



# 本题要求读入 N 名学生的成绩，将获得某一给定分数的学生人数输出。

