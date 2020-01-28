n = int(input())
nums = list(map(int,input().split()))
MainList = []
MaxNum = nums[0]

for i in range(n-1) :
    if nums[i] >= MaxNum :
        if min(nums[i+1:]) > nums[i]:
            MainList.append(nums[i])
        MaxNum = nums[i]        
if MaxNum < nums[-1] :
    MainList.append(nums[-1])

print(len(MainList))
for i in range(len(MainList)-1) :
    print(MainList[i],end=' ')
if len(MainList) > 0 : 
    print(MainList[-1])
else :
    print('\n',end='')

