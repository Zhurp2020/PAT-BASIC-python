a, b = input().split()
NumDict = {10:'J',11:'Q',12:'K'}
res = ''

if len(b) < len(a) :
    for i in range(len(a)-len(b)) :
        b = b.join(['0',''])
for i in range(1,len(a)+1) :
    if i % 2 != 0 :
        temp = (int(a[-i]) + int(b[-i])) % 13
        if temp in NumDict :
            temp = NumDict[temp]
    else :
        temp = int(b[-i]) - int(a[-i])
        if temp <0 :
            temp += 10
    res = res.join([str(temp),''])

if len(b)>len(a)  :
    res = res.join([b[0:len(b)-len(a)],''])
print(res)