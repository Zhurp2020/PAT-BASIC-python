n = int(input())
studentdict = {}
for i in range(n) :
    student = input().split()
    studentdict[student[1]] = (student[0],student[2])
n2 = int(input())
tocheck = input().split()

for i in range(n2) :
    print(studentdict[tocheck[i]][0],studentdict[tocheck[i]][1])



# 每个 PAT 考生在参加考试时都会被分配两个座位号，一个是试机座位，
# 一个是考试座位。正常情况下，考生在入场时先得到试机座位号码，
# 入座进入试机状态后，系统会显示该考生的考试座位号码，
# 考试时考生需要换到考试座位就座。但有些考生迟到了，试机已经结束，
# 他们只能拿着领到的试机座位号码求助于你，从后台查出他们的考试座位号码。