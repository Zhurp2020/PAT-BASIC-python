m = int(input())
numbers = [int(i) for i in input().split()]

for i in numbers:
    flag = False
    for n in range(10) :
        num = str(n * (i **2))
        if num[len(num)-len(str(i)):] == str(i) :
            print(n,num)
            flag = True
            break
    if not flag :
        print('No')
