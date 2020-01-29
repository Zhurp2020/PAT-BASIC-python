number = int(input())
nums = list(map(int,input().split()))
nums.sort(reverse=True)
def findmn(num) :
    mnList = []
    for n in range(1,num):
        if num % n== 0 :
            m = num // n
            if m >= n :
                mnList.append((m,n))
            else :
                break
    return min(mnList, key= lambda elem:elem[0] - elem[1])

if number == 1:
    m = n = 1
else :
    mn = findmn(number)
    m,n = mn[0],mn[1]
result = [[0 for i in range(n)] for j in range(m)]
i = 0
j = 1
line = m-1
column = n
while i < number  :
    position = j //4
    if j % 4 == 1 :
        result[position][position:position+column] = nums[i:i+column]
        j += 1 
        i += column
        column -= 1
    elif j % 4 == 2 :
        for aline in result[position+1:position+1+line] :
            aline[n-position-1] = nums[i]
            i += 1
        j += 1
        line -= 1    
    elif j % 4 == 3 :
        result[m-position-1][position:position+column] = nums[i+column-1:i-1:-1]
        j += 1
        i += column
        column -= 1
    elif j % 4 == 0:
        for aline in result[m-position-1:m-position-line-1:-1]:
            aline[position-1] = nums[i]
            i += 1
        j += 1
        line -= 1

for aline in result :
    res = ' '.join(list(map(str,aline)))
    print(res)

        




