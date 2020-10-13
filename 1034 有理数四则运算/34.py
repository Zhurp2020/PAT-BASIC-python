a,b = input().split()
a1,a2 = list(map(int,a.split('/')))
b1,b2 = list(map(int,b.split('/')))
def gcd(num1,num2) :
    if num1 > num2 :
        num1,num2 = num2, num1
    while num2 :
        num1,num2 = num2,num1 % num2
    return num1
def lcm(num1,num2) :
    return num1 * num2 // gcd(num1,num2)
def simplfy (num1,num2) :
    res = ''
    if num1 < 0 :
        res = '-' + res
    num3,num4 = abs(num1) % num2,abs(num1) // num2
    if num3 == 0 :
        res += str(int(num4))
        return res
    if abs(num1) > num2 :
        res += str(int(num4)) + ' '
        num1 = num3
    numgcd = gcd(abs(num1),num2)
    if numgcd != 1 :
        num1,num2 = abs(num1) / numgcd,num2 / numgcd
    res += str(int(abs(num1))) + '/' + str(int(num2))
    return res
def sumsub (num1,num2,num3,num4) :
    numlcm = lcm(num2,num4)
    multi1,multi2 = numlcm / num2,numlcm / num4
    num1,num2,num3,num4 = num1*multi1,num2*multi1,num3*multi2,num4*multi2
    sum1,sum2 = num1 + num3,num2
    sub1,sub2 = num1 - num3,num2
    return [simplfy(sum1,sum2),simplfy(sub1,sub2)] 
def multidiv (num1,num2,num3,num4) :
    multi1,multi2 = num1 * num3,num2 * num4
    if num3 == 0 :
        return [simplfy(multi1,multi2),'Inf']
    else :
        divide1,divide2 = num1*num4,num2*num3
        if divide2 < 0 :
            divide1,divide2 = -divide1,-divide2
        return [simplfy(multi1,multi2),simplfy(divide1,divide2)]
def checkminus (string) :
    if string[0] == '-' :
        return '(' + string + ')'
    else :
        return string

res1 = sumsub(a1,a2,b1,b2)
res2 = multidiv(a1,a2,b1,b2)
a,b = simplfy(a1,a2),simplfy(b1,b2)
answers = list(map(checkminus,[res1[0],res1[1],res2[0],res2[1],a,b]))
b = answers[5]
a = answers[4]
print(a,'+',b,'=',answers[0])
print(a,'-',b,'=',answers[1])
print(a,'*',b,'=',answers[2])
print(a,'/',b,'=',answers[3])



# 本题要求编写程序，计算 2 个有理数的和、差、积、商。