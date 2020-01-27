InputString = input()
AlphaDict = {}

for i in InputString :
    if i.isalpha() :
        iLower = i.lower()
        if not(iLower in AlphaDict) :
            AlphaDict[iLower] = 1
        else :
            AlphaDict[iLower] += 1
AlphaList = sorted(AlphaDict.items(), key= lambda elem:elem[0])
MaxAlpha = max(AlphaList,key= lambda elem:elem[1])

print(MaxAlpha[0],MaxAlpha[1])       