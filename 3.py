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


#“答案正确”是自动判题系统给出的最令人欢喜的回复。
# 本题属于 PAT 的“答案正确”大派送 —— 只要读入的字符串满足下列条件，
# 系统就输出“答案正确”，否则输出“答案错误”。
#得到“答案正确”的条件是：
#字符串中必须仅有 P、 A、 T这三种字符，不可以包含其它字符；
#任意形如 xPATx 的字符串都可以获得“答案正确”，其中 x 或者是空字符串，或者是仅由字母 A 组成的字符串；
#如果 aPbTc 是正确的，那么 aPbATca 也是正确的，其中 a、 b、 c 均或者是空字符串，或者是仅由字母 A 组成的字符串。
#现在就请你为 PAT 写一个自动裁判程序，判定哪些字符串是可以获得“答案正确”的。