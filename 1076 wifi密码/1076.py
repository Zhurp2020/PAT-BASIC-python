n = int(input())
pwddict = {'A':'1','B':'2','C':'3','D':'4'}
res = ''

for i in range(n):
    answers = input().split()
    for j in answers:
        if j[2] == 'T' :
            res += pwddict[j[0]]

print(res)