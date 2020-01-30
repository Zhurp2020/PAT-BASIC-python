import re
match = re.compile(r'\[.*?]')
SymbolList = []
def stripstr (string) :
    a = string.lstrip('[')
    a = a.rstrip(']')
    return a
for i in range(3) :
    MatchList = match.findall(input())
    SymbolList.append(list(map(stripstr,MatchList)))

n = int(input())
for i in range(n) :
    res = ''
    nums = list(map(int,input().split()))
    if nums[0] >len(SymbolList[0]) or nums[1] > len(SymbolList[1]) or nums[2] > len(SymbolList[2]) or nums[3] > len(SymbolList[1]) or nums[4] > len(SymbolList[0]) :
        print('Are you kidding me? @\/@')
    else :
        res += SymbolList[0][nums[0]-1]
        res += '(' + SymbolList[1][nums[1]-1]
        res += SymbolList[2][nums[2]-1]
        res += SymbolList[1][nums[3]-1] + ')'
        res += SymbolList[0][nums[4]-1]
        print(res)


