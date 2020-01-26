n = input().split()
for i in range(len(n)) :
    n[i] = int(n[i])
a=[0,0,0,0,0]
a2num = 0
a4num = 0
temp = [0,2,3,4]

for i in range(1,len(n)) :
    if n[i] % 5 == 0 and n[i] % 2 == 0 :
        a[0] = a[0] + n[i]
    elif n[i] % 5 == 1 :
        a2num = a2num + 1
        a[1] = a[1] + n[i] * ((-1)**(a2num+1))
    elif n[i] % 5 == 2 :
        a[2] = a[2]+1
    elif n[i] % 5 == 3 :
        a4num = a4num +1
        a[3] = a[3] + n[i]
    elif n[i] % 5 == 4 :
        if n[i] > a[4] :
            a[4] = n[i]
if a2num == 0 :
    a[1] = 'N'
for i in temp :
    if a[i] == 0 :
        a[i] = 'N'

if a[3] != 'N' :
    print('{} {} {} {:.1f} {}'.format(a[0],a[1],a[2],a[3]/a4num,a[4]))
else :
    print('{} {} {} N {}'.format(a[0],a[1],a[2],a[4]))

