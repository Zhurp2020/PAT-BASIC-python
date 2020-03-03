n = int(input())
maxn = ''
minn = ''
NameNumScr = {}
for i in range (n) :
    a, b, c = input().split()
    NameNumScr [int(c)] = a+' '+b

maxn = NameNumScr.get(max(NameNumScr.keys()))
minn = NameNumScr.get(min(NameNumScr.keys()))

print(maxn)
print(minn)
