n = int(input())
studentdict = {i+1:0 for i in range(n)}
for i in range(n) :
    student,scroe = list(map(int,input().split()))
    studentdict[student] += scroe

maxstudent = max(studentdict.items(),key= lambda elem : elem[1])

print(maxstudent[0],maxstudent[1])



# 为了用事实说明挖掘机技术到底哪家强，PAT 组织了一场挖掘机技能大赛。
# 现请你根据比赛结果统计出技术最强的那个学校。