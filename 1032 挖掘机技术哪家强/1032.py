n = int(input())
studentdict = {i+1:0 for i in range(n)}
for i in range(n) :
    student,scroe = [int(i) for i in input().split()]
    studentdict[student] += scroe

maxstudent = max(studentdict.items(),key= lambda elem : elem[1])

print(maxstudent[0],maxstudent[1])

