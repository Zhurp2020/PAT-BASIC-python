num = input()
def ispalinum (string):
    if string == string [::-1]:
        return True
    else:
        return False

if ispalinum(num):
    print('{} is a palindromic number.'.format(num))
    exit()
for i in range(10):
    temp = str(int(num) + int(num[::-1]))
    print('{} + {} = {}'.format(num,num[::-1],temp))
    if ispalinum(temp) :
        print('{} is a palindromic number.'.format(temp))
        exit()
    num = temp
print('Not found in 10 iterations.')
