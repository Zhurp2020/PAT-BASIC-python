StringIn = input()
alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alpdict = {alp[i-1]:i for i in range(1,27)}
n = 0

for i in StringIn :
    if i.isalpha() :
        n += alpdict[i.lower()]
nBin = str(bin(n)).lstrip('0b')
cou0 = nBin.count('0')

print(cou0,len(nBin)-cou0)