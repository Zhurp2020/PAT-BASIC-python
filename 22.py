a,b,d = list(map(int,input().split()))
def convert(num,rule) :
    if num < rule :
        return num
    res = ''
    while True :
        temp1 = num // rule
        temp2 = num % rule
        if temp1 >= rule :
            res = str(temp2) + res
        else :
            res = str(temp1) + str(temp2) + res
            break
        num = temp1
    return res

sum = a+b
out = convert(sum,d)

print(out)



# 输入两个非负 10 进制整数 A 和 B (≤230−1)，输出 A+B 的 D (1<D≤10)进制数