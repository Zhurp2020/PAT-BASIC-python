n,symbol = input().split()
n = int(n)
def numsymbol(num) :
    if num == 1 :
        return 1
    else :
        return 2 * num + numsymbol(num-2)
numnow = 1
topnum = 1

while True :
    numnow = numsymbol(topnum)
    if numnow <= n :
        topnum += 2
    else :
        topnum -= 2
        break

for i in range(topnum,1,-2) :
    print('{:^{}}'.format(symbol*i,topnum).rstrip())
for i in range(1,topnum+2,2) :
    print('{:^{}}'.format(symbol*i,topnum).rstrip())
print(n-numsymbol(topnum))  



# 本题要求你写个程序把给定的符号打印成沙漏的形状。
# 例如给定17个“*”，要求按下列格式打印
# *****
#  ***
#   *
#  ***
# *****
# 所谓“沙漏形状”，是指每行输出奇数个符号；各行符号中心对齐；
# 相邻两行符号数差2；符号数先从大到小顺序递减到1，
# 再从小到大顺序递增；首尾符号数相等。
# 给定任意N个符号，不一定能正好组成一个沙漏。
# 要求打印出的沙漏能用掉尽可能多的符号。