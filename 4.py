n = int(input())
maxn = ''
minn = ''
NameNumScr = {}
for i in range (n) :
    a, b, c = input().split()
    NameNumScr [int(c)] = a+' '+b

maxn = NameNumScr.get(max(NameNumScr.keys()))
minn = NameNumScr.get(min(NameNumScr.keys()))

print(maxn)
print(minn)



# 读入 n（>0）名学生的姓名、学号、成绩，分别输出成绩最高和成绩最低学生的姓名和学号。