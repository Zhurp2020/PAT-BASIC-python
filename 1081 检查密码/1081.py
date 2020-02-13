n = int(input())

for i in range(n) :
    password = input()
    needalpha = True
    neednumber = True
    legit = True
    if len(password) < 6 :
        print('Your password is tai duan le.')
    else :
        for j in password :
            if j.isalpha() :
                needalpha = False
            elif j.isdigit() :
                neednumber = False
            elif  j != '.' :
                print('Your password is tai luan le.')
                legit = False
                break
        if needalpha and legit:
            print('Your password needs zi mu.')
        elif neednumber and legit:
            print('Your password needs shu zi.')
    if legit and (not needalpha) and (not neednumber) :
        print('Your password is wan mei.')
