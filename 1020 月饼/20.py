Flavor,MaxDemand = list(map(int,input().split()))
StorageAmount = list(map(float,input().split()))
prices = list(map(float,input().split()))
SellAmount = 0
Maxrevenue = 0

MoonCake = [[StorageAmount[i],prices[i]/StorageAmount[i]] for i in range(Flavor)]
MoonCake.sort(key= lambda elem:elem[1],reverse=True)
for i in MoonCake :
    SellAmount = SellAmount + i[0]
    if SellAmount <= MaxDemand :
        Maxrevenue = i[0] * i[1] + Maxrevenue
    else:
        Maxrevenue = (i[0]-(SellAmount-MaxDemand))*i[1] + Maxrevenue
        break
    
print('{:.2f}'.format(Maxrevenue))



# 月饼是中国人在中秋佳节时吃的一种传统食品，
# 不同地区有许多不同风味的月饼。现给定所有种类月饼的库存量、总售价、
# 以及市场的最大需求量，请你计算可以获得的最大收益是多少。
# 注意：销售时允许取出一部分库存。样例给出的情形是这样的：
# 假如我们有 3 种月饼，其库存量分别为 18、15、10 万吨，
# 总售价分别为 75、72、45 亿元。如果市场的最大需求量只有 20 万吨，
# 那么我们最大收益策略应该是卖出全部 15 万吨第 2 种月饼、
# 以及 5 万吨第 3 种月饼，获得 72 + 45/2 = 94.5（亿元）。


