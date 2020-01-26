n = int(input())
nums = []
nums2 = []
res = ''
nums[:n] = input().split()
def calc(a):
   if a % 2 == 1 :
      return (3 * a + 1) / 2
   else :
      return a/2

for i in range(n) :
    nums[i] = int(nums[i])
    nums2.append(nums[i])
for i in range(n) :
    while nums[i] != 1 :
        nums[i] = calc(nums[i])
        if nums[i] in nums2 :
            nums2.remove(nums[i])
nums2.sort(reverse=True)

for i in nums2 :
    res = res + str(i) + ' '
print(res.rstrip(' '))


#卡拉兹(Callatz)猜想已经在1001中给出了描述。在这个题目里，情况稍微有些复杂。
#当我们验证卡拉兹猜想的时候，为了避免重复计算，可以记录下递推过程中遇到的每一个数。
# 例如对 n=3 进行验证的时候，我们需要计算 3、5、8、4、2、1，
# 则当我们对 n=5、8、4、2 进行验证的时候，就可以直接判定卡拉兹猜想的真伪，
# 而不需要重复计算，因为这 4 个数已经在验证3的时候遇到过了，
# 我们称 5、8、4、2 是被 3“覆盖”的数。
# 我们称一个数列中的某个数 n 为“关键数”，如果 n 不能被数列中的其他数字所覆盖。
# 现在给定一系列待验证的数字，我们只需要验证其中的几个关键数，
# 就可以不必再重复验证余下的数字。你的任务就是找出这些关键数字，并按从大到小的顺序输出它们。

