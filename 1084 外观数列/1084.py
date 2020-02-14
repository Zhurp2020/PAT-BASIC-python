d,n = input().split()
def genNext (string) :
    res = ''
    i = 0
    while i <= len(string) -1 :
        count = 1
        while i <= len(string) -2:
            if string[i] == string[i+1] :
                i += 1
                count += 1
            else :
                break
        res += string[i] + str(count)
        i += 1
    return res 

for i in range(int(n)-1) :
    res = genNext(d)
    d = res

if n == '1' :
    print(d)    
else:
    print(res)