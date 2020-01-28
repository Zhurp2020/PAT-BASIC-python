n = int(input())
nums = list(map(int,input().split()))
MainList = []
MaxNum = nums[0]

for i in range(n) :
    if nums[i] >= MaxNum :
            MainList.append(nums[i])
            MaxNum = nums[i]  
    else : 
        if len(MainList) != 0 :     
            while nums[i] <= MainList[-1] :
                MainList.remove(MainList[-1])  
                if len(MainList) == 0 :
                    break
        
print(len(MainList))
for i in range(len(MainList)-1) :
    print(MainList[i],end=' ')
if len(MainList) > 0 : 
    print(MainList[-1])
else :
    print('\n',end='')

