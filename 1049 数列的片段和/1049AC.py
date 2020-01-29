n = int(input())
m = [float(i) for i in input().split()]
rst = 0
for i in range(n):
    rst += m[i] * (n - i) * (i + 1)
print('{:.2f}'.format(rst))

