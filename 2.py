n = input()
ans = 0
res = ' '
NumPinYin = ['ling ','yi ','er ','san ','si ','wu ','liu ','qi ','ba ','jiu ']

for a in n :
    ans = ans + int(a)
ans = str(ans)
for c in ans :
    res = res + NumPinYin[int(c)]

print (res.strip(' '))



#读入一个正整数 n，计算其各位数字之和，用汉语拼音写出和的每一位数字。