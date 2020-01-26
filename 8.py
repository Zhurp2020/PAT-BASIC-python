n,m = input().split()
n = int(n)
m = int(m)
nums = []
nums[:n] = input().split()
res = ''
for i in range(n) :
    nums[i] = int(nums[i])
if m > n :
    m = m % n

for i in range(m) :
    nums.append(0)
for i in range(n+m-1,m-1,-1) :
    nums[i] = nums [i-m]
for i in range(m) :
    nums[i],nums[i+n] = nums[i+n],nums[i]
for i in range(n+m-1,n-1,-1) :
    del nums[i]

for i in nums :
    res = res +str(i) +' '
print(res.rstrip())



# 一个数组A中存有N（>0）个整数，在不允许使用另外数组的前提下，
# 将每个整数循环向右移M（≥0）个位置，即将A中的数据由（A0A1⋯A​N−1）
# 变换为（AN−M⋯A​N−1A0A1⋯A​N−M−1）（最后M个数循环移至最前面的M个位置）。
# 如果需要考虑程序移动数据的次数尽量少，要如何设计移动的方法？