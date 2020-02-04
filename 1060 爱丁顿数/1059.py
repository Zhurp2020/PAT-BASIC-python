n = int(input())
nums = list(map(int,input().split()))
e = 0

nums.sort(reverse= True)
for i in nums :
    if i > e + 1 :
        e += 1

print(e)
     