n = int(input())
record = []
awinrec = []
bwinrec = []
win = 0
nowin = 0
for i in range(n) :
    record.append(input().split())
def checkwin (gesture) :
    if gesture [0] == gesture[1] :
        return 3
    else :
        if 'C' in gesture :
            if 'B' in gesture :
                return gesture.index('B')
            else :
                return gesture.index('C')
        else :
            return gesture.index('J')

for i in record :
    if checkwin(i) == 0 :
        win = win + 1
        awinrec.append(i[0])
    elif checkwin(i) == 3 :
        nowin = nowin + 1
    else :
        bwinrec.append(i[1])
amax = max(awinrec.count('Ç'),awinrec.count('B'),awinrec.count('J'))
bmax = max(bwinrec.count('Ç'),bwinrec.count('B'),bwinrec.count('J'))
for i in ['B','C','J'] :
    if awinrec.count(i) == amax :
        awin = i
        break
for i in ['B','C','J'] :
    if bwinrec.count(i) == bmax :
        bwin = i
        break

print(win,nowin,n-win-nowin)
print(n-win-nowin,nowin,win)
print(awin,bwin)
