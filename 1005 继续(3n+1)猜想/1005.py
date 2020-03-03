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

