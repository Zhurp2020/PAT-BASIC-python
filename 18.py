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

# 大家应该都会玩“锤子剪刀布”的游戏：两人同时给出手势，胜负规则如图所示：
# 现给出两人的交锋记录，
# 请统计双方的胜、平、负次数，并且给出双方分别出什么手势的胜算最大。