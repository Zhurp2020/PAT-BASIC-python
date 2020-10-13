n = input()
numdict = {i:0 for i in range(10)}
res = []

for i in n :
    numdict[int(i)] +=  1
for i in numdict :
    if numdict[i] > 0 :
        res.append((i,numdict[i]))
res.sort()

for i in res :
    print('{}:{}'.format(*i))



# 给定一个 k 位整数 N=dk−110k−1+⋯+d1101+d0(0≤di≤9, i=0,⋯,k−1, dk−1>0)，
# 请编写程序统计每种不同的个位数字出现的次数。例如：给定 N=100311，
# 则有 2 个 0，3 个 1，和 1 个 3。