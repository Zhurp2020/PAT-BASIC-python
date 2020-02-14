a,b = [int(i) for i in input().split()]

print(str(a*b)[::-1].lstrip('0'))