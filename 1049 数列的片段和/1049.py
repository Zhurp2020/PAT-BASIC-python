n = int(input())
nums = input().split()
result = 0

for i in range(n):
    flag = True
    j = 0
    while flag and j < n:
        TempList = [nums[i]]
        for k in range(i,j) :
            if int(nums[k][-1]) - int(nums[k+1][-1]) == -1 and len(nums[k]) == len(nums[k+1]) :
                TempList.append(nums[k+1])
            else :
                flag = False
                break
        if flag :
            result += sum(list(map(float,TempList)))
        if j < i :
            j = i
        j += 1

print('{:.2f}'.format(result))