a,da,b,db = input().split()
pa = ''
pb = ''

for i in a :
    if i == da :
        pa = pa +i
for i in b :
    if i == db :
        pb = pb +i
if pa == '' :
    pa = 0
if pb == '' :
    pb = 0
ans = int(pa) + int(pb)

print(ans)



#正整数 A 的“DA（为 1 位整数）部分”定义为由 A 中所有DA组成的新整数 PA。
# #例如：给定 A=3862767，DA=6，则 A 的“6 部分”PA​​是 66，
# 因为 A 中有 2 个 6。现给定 A、DA 、B、DB ，请编写程序计算PA+PB。