nums = input().split()
nsum = 0

for i in range(1,int(nums[0])+1) :
    for j in range(1,int(nums[0])+1):
        if i != j :
            nsum += int(nums[i]+nums[j])

print(nsum)

