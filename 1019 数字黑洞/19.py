n = input()
n = '0'*(4 - len(n))+n
nint = int(n)

if n[0] == n[1] == n[2] == n[3] :
    print('{} - {} = 0000'.format(n,n)) 
elif nint == 6174:
    print('7641 - 1467 = 6174')
else:
    while nint != 6174 :
        nlist = []
        nstr1 = ''
        nstr2 = ''
        for i in n :
            nlist.append(i)
        nlist.sort(reverse= True)
        for i in nlist :
            nstr1 = nstr1 + i
        nlist.sort()
        for i in nlist :
            nstr2 = nstr2 + i
        nint = int(nstr1) - int(nstr2)
        n = str(nint)
        n = '0'*(4 - len(n))+n
        print('{} - {} = {}'.format(nstr1,nstr2,n))



#给定任一个各位数字不完全相同的 4 位正整数，
# 如果我们先把 4 个数字按非递增排序，再按非递减排序，
# 然后用第 1 个数字减第 2 个数字，将得到一个新的数字。
# 一直重复这样做，我们很快会停在有“数字黑洞”之称的 6174，
# 这个神奇的数字也叫 Kaprekar 常数。
    
