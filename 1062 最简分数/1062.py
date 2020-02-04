a,b,k = input().split()
frac1 = eval(a)
frac2 = eval(b)
if frac2 < frac1 :
    frac1,frac2 = frac2,frac1
k = int(k)
def gcd(num1,num2) :
    if num1 > num2 :
        num1,num2 = num2, num1
    while num2 :
        num1,num2 = num2,num1 % num2
    return num1
res = ''
i = 0

while True :
    if frac2 > i / k > frac1 :
        if gcd(i,k) == 1 and i != k:
            res += str(i) + '/' + str(k) + ' '
    if frac2 < i/k :
        break
    i += 1

print(res.rstrip())