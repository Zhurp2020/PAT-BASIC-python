a,b = input().split()
P = list(map(int,a.split('.')))
A = list(map(int,b.split('.')))

flag = False
if A[0] < P[0] or (A[0] == P[0] and A[1] < P[1]) or (A[0] == P [0] and A[1] == P[1] and A[2] < P[2]):
    flag = True
    A,P =P,A
knut = A[2] - P[2]
if knut < 0 :
    knut = 29 + knut
    A[1] -= 1
sickle = A[1] - P[1]
if sickle < 0 :
    sickle = 17 + sickle
    A[0] -= 1
galleon = A[0] -P[0]
if flag :
    galleon = -galleon

print('{}.{}.{}'.format(galleon,sickle,knut))



# 如果你是哈利·波特迷，你会知道魔法世界有它自己的货币系统 —— 
# 就如海格告诉哈利的：“十七个银西可(Sickle)兑一个加隆(Galleon)，
# 二十九个纳特(Knut)兑一个西可，很容易。”现在，
# 给定哈利应付的价钱 P 和他实付的钱 A，
# 你的任务是写一个程序来计算他应该被找的零钱。

