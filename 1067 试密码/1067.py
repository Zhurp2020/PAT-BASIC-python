password,maxtry= input().split()
maxtry = int(maxtry)
count = 0
end = False

while True :
    psw = input()
    if psw == '#' :
        exit()   
    elif psw == password:
        print('Welcome in')
        exit()
    else :
        print('Wrong password: {}'.format(psw))
        count += 1
    if count == maxtry:
        print('Account locked')
        exit()

    