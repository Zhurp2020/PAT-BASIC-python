import math
nums = list(map(float,input().split()))

a1,b1 = nums[0]*math.cos(nums[1]),nums[0]*math.sin(nums[1])
a2,b2 = nums[2]*math.cos(nums[3]),nums[2]*math.sin(nums[3])
complexa = complex(a1,b1)
complexb = complex(a2,b2)
complexc = complexa * complexb
a = round(complexc.real,2)
b = round(complexc.imag,2)
if a == 0 :
    a = 0
if b == 0 :
    b = 0

if b>=0 :
    print('{:.2f}+{:.2f}i'.format(a,b))
else :
    print('{:.2f}{:.2f}i'.format(a,b))