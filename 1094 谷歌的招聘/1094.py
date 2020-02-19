import math
l,k = [int(i) for i in input().split()]
string = input()
def isprime(num) :
    for i in range(2,int(math.sqrt(num))+1) :
        if num % i == 0 :
            return False 
    return True

for i in range(1,l-k+2) :
    num = string[i-1:i+k-1] 
    if isprime(int(num)) :
        print(num)
        exit()

print('404')
