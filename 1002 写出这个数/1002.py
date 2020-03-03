n = input()
ans = 0
res = ' '
NumPinYin = ['ling ','yi ','er ','san ','si ','wu ','liu ','qi ','ba ','jiu ']

for a in n :
    ans += int(a)
ans = str(ans)
for c in ans :
    res += NumPinYin[int(c)]

print (res.strip(' '))

