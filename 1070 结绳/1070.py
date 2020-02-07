n = int(input())
nums = list(map(int,input().split()))

nums.sort()
length = nums[0]
for i in range(1,n) :
    length = (length+nums[i])/2

print(int(length))