n = int(input())
res = set()

for i in range(1,n+1) :
    res.add(sum([int(i/2),int(i/3),int(i/5)]))

print(len(res))