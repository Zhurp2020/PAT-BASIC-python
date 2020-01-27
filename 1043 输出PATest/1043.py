InPutString = input()
PATlist = ('P','A','T','e','s','t')
PATdict = {i:0 for i in PATlist}
count = 0

for i in InPutString :
    if i in PATdict :
        PATdict[i] += 1
        count += 1
for i in range(count) :
    for j in range(6) :
        if PATdict[PATlist[j]] > 0 :
            print(PATlist[j],end='')
            PATdict[PATlist[j]] -= 1

