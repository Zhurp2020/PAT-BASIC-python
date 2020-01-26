n,p = list(map(int,input().split()))
nums = list(map(int,input().split()))
count = 0
countmax = count

for m in nums :
    for j in nums :
        if m <= j <= m * p :
            count += 1
    if count > countmax :
        countmax = count
    if countmax == len(nums) :
        break
    count = 0

print(countmax)


# x = [int(i) for i in input().split()]
# n = sorted(map(int, input().split()))
# m = 1
# for i in range(x[0]):
#     while m + i < x[0]:
#         if n[i] * x[1] >= n[i + m]:
#             m += 1
#         else:
#             break
# print(m)



# 给定一个正整数数列，和正整数 p，设这个数列中的最大值是 M，
# 最小值是 m，如果 M≤mp，则称这个数列是完美数列。
# 现在给定参数 p 和一些正整数，请你从中选择尽可能多的数构成一个完美数列。