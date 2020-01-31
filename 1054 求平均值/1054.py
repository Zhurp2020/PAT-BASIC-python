n = int(input())
nums = input().split()
k = 0
numsum = 0
class ilegalERR(ValueError) :
    pass
def checknum(num) :
    if num > 1000 or num < -1000 :
        raise ilegalERR()
    a,b = str(num).split('.')
    if len(b) > 2:
        raise ilegalERR()
    return True

for i in nums :
    try :
        temp = float(i)
        if checknum(temp) :
            k += 1
            numsum += temp
    except :
        print('ERROR: {} is not a legal number'.format(i))

try:
    avg = numsum / k
    if k != 1 :
        print('The average of {} numbers is {:.2f}'.format(k,avg))
    else:
        print('The average of 1 number is {:.2f}'.format(avg))
except :
    print('The average of 0 numbers is Undefined')