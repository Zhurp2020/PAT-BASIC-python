rulelist = input()
num1 = input().rjust(len(rulelist),'0')
num2 = input().rjust(len(rulelist),'0')
res = ''

plus = 0
for i in range(1,len(rulelist)+1) :
    temp = int(num1[-i])+int(num2[-i])+plus
    if rulelist[-i] == '0' :
        rule = 10
    else :
        rule = int(rulelist[-i])
    if temp >= rule :
        plus = 1
        temp = temp-rule
    else :
        plus = 0
    res = str(temp) + res
if plus == 1 :
    res = '1'+res

ans = res.lstrip('0')
if len(ans) == 0 :
    print('0')
else: 
    print(ans)