n = int(input())
def whowin(aHan,aHua,bHan,bHua) :
    if aHua == aHan + bHan == bHua:
        return None
    elif bHua == aHan + bHan :
        return 'B'
    elif aHua == aHan + bHan:
        return 'A'
counta = countb = 0

for i in range(n) :
    nums = list(map(int,input().split()))
    result = whowin(nums[0],nums[1],nums[2],nums[3])
    if result == 'A' :
        countb += 1
    if result == 'B' :
        counta += 1
    
print(counta,countb)