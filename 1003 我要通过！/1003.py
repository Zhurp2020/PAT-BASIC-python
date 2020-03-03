n = int(input())
InPutStore = []
for i in range (n) :
    InPutStore.append(input())

def check1(example) :
    for char in example :
        if char != 'P' and char != 'A' and char != 'T' :
            return False
    return True 
def checklen3(example) :
    if len(example)<3 :
        return False
    else :
        return True
def ischeck2 (example) :
    for i in range(len(example)-2) :
        if example[i:i+3] == 'PAT' :
            return True
    return False
def check2(example) :
    x1 = ''
    x2 = ''
    for i in range(len(example)-2) :
        if example[i:i+3] == 'PAT' :
            x1 = example[0:i]
            x2 = example[i+3:len(example)]
            break
    for char in x1 :
        if char != 'A' :
            return False
    for char in x2 :
        if char != 'A' :
            return False
    if x1 == x2 :
        return True
    else :
        return False
def handle3(example) :
    a = ''
    b = ''
    c = ''
    Pposition = 0
    for i in range(len(example)-1) :    
        if example[i] == 'P' :
            a = example[0:i]
            Pposition = i
        if example[i:i+2] == 'AT' :
            b = example[Pposition+1:i]
            c = example[i+2:len(example)-len(a)]
            return a+'P'+b+'T'+c
    return False

for string in InPutStore :
    if (checklen3 == False) or (check1(string) == False) :
        print('NO')
    else :
        while ischeck2(string) == False :
            string = handle3(string)
            if string == False :
                break
        if string == False :
            print('NO')
        elif check2(string) :
            print ('YES')
        else :
            print('NO')
