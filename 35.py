n = int(input())
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
flag = True

for i in range(n//2) :
    temp = [list2[i*2],list2[i*2+1]]
    temp.sort()
    if temp == [list2[i*2],list2[i*2+1]] :
        continue
    else :
        flag = False
        break

if flag :
    print('Merge Sort')
    count = 4
    reslist = []
    while True :
        for i in range(n // count) :
            templist = list2[count*i:count*(i+1)]
            templist.sort()
            reslist += templist
        if n % count != 0 :
            templist = list2[-(n%count):]
            templist.sort()
            reslist += templist
        if reslist != list2 :
            break
        else :
            count = count *2
            reslist = []
else :
    print('Insertion Sort')
    for i in range(n-1) :
        if list2[i] > list2[i+1] :
            reslist = list2[:i+2]
            reslist.sort()
            reslist += list2[i+2:]
            break

res = ''
for i in reslist :
    res += str(i) + ' '
print(res.rstrip())



# 根据维基百科的定义：
# 插入排序是迭代算法，逐一获得输入数据，逐步产生有序的输出序列。
# 每步迭代中，算法从输入序列中取出一元素，将之插入有序序列中正确的位置。
# 如此迭代直到全部元素有序。
# 归并排序进行如下迭代操作：
# 首先将原始序列看成 N 个只包含 1 个元素的有序子序列，
# 然后每次迭代归并两个相邻的有序子序列，直到最后只剩下 1 个有序的序列。
# 现给定原始序列和由某排序算法产生的中间序列，
# 请你判断该算法究竟是哪种排序算法？