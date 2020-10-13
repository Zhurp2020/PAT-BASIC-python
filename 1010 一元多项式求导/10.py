n = input()
countspace = 0
nums = []
res = ''
is0 = 0
for char in n :
    if char == ' ' :
        countspace = countspace + 1
nums [:countspace+1] = n.split()

for i in range(0,len(nums),2) :
    if nums[i] == '0' and is0 == 0:
        res = res +'0 0 '
        is0 = 1
    elif nums[i+1] != '0' and nums[i] != '0':
        res = res + str(int(nums[i])*int(nums[i+1]))+' '+str(int(nums[i+1])-1)+' '
if n == '':
    print('0 0')
elif len(nums) == 2 and nums[1] == '0' :
    print('0 0')
else :
    print(res.rstrip())

#设计函数求一元多项式的导数。（注：xn（n为整数）的一阶导数为nxn−1。）