inputlist = list(map(int,input().split()))
numlist = []
res = ''

for i in range(inputlist[0]) :
    res += '0'
for i in range(1,10) :
    for j in range(inputlist[i]) :
        numlist.append(i)
res = str(numlist[0]) + res 
for i in range(1,len(numlist)) :
    res += str(numlist[i])

print(res)



# 给定数字 0-9 各若干个。你可以以任意顺序排列这些数字，
# 但必须全部使用。目标是使得最后得到的数尽可能小（注意 0 不能做首位）。
# 例如：给定两个 0，两个 1，三个 5，一个 8，
# 我们得到的最小的数就是 10015558。
# 现给定数字，请编写程序输出能够组成的最小的数。