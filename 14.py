a = input()
b = input()
c = input()
d = input()
m = 1
daydict = {'A':'MON','B':'TUE','C':'WED','D':'THU','E':'FRI','F':'SAT','G':'SUN'}
hourdict = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':18,'J':19,'K':20,'L':21,'M':22,'N':23}

for i in range(min(len(a),len(b))) :
    if a[i] == b[i] and m == 1 and a[i] in daydict:
        day = daydict[a[i]]
        m = 2
        continue
    if a[i] == b[i] and m == 2 and  (a[i] in hourdict or a[i].isdigit()):
        if a[i] in hourdict :
            hour = hourdict[a[i]] 
        elif 0 <= int(a[i]) <= 9 :
            hour = '0' + str(a[i])
        break
for i in range(min(len(c),len(d))) :
    if c[i] == d[i] and c[i].isalpha()  :
        if i < 10 :
            minute = '0' + str(i)
        else :
            minute = i
        break

print('{} {}:{}'.format(day,hour,minute))



# 大侦探福尔摩斯接到一张奇怪的字条：我们约会吧！ 
# 3485djDkxh4hhGE 2984akDfkkkkggEdsb s&hgsfdk d&Hyscvnm。
# 大侦探很快就明白了，字条上奇怪的乱码实际上就是约会的时间星期四 14:04，
# 因为前面两字符串中第 1 对相同的大写英文字母（大小写有区分）是第 4 个字母
#  D，代表星期四；第 2 对相同的字符是 E ，那是第 5 个英文字母，
# 代表一天里的第 14 个钟头（于是一天的 0 点到 23 点由数字 0 到 9、
# 以及大写字母 A 到 N 表示）；
# 后面两字符串第 1 对相同的英文字母 s 出现在第 4 个位置（从 0 开始计数）
# 上，代表第 4 分钟。现给定两对字符串，请帮助福尔摩斯解码得到约会的时间。