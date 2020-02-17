m,x,y = [int(i) for i in input().split()]
res = ['','','']

for i in range(99,9,-1) :
    a = i
    b = int(str(i)[::-1])
    c = abs(a-b)/x
    if c == b / y :
        power = [a,b,c]
        break

try :
    for i in range(3) :
        if power[i] > m :
            res[i] = 'Cong'
        elif power[i] == m :
            res[i] = 'Ping'
        else:
            res[i] = 'Gai'
    print(power[0],' '.join(res))
except :
    print('No Solution')