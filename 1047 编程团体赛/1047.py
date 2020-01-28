n = int(input())
TeamDict = {}

for i in range(n) :
    student = input().split()
    StuNum = student[0].split('-')
    if StuNum[0] in TeamDict :
        TeamDict[StuNum[0]] += int(student[1])
    else :
        TeamDict[StuNum[0]] = int(student[1])
MaxTeam = max(TeamDict.items(), key= lambda elem:elem[1])

print(MaxTeam[0],MaxTeam[1])
