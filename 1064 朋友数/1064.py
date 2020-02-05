n = int(input())
nums = input().split()
def sumnum(string) :
    return sum(list(map(int,string)))

FriList = list(set(map(sumnum,nums)))
FriList.sort()

print(len(FriList))
print(' '.join(map(str,FriList)))