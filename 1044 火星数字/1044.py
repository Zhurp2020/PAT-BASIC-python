List1 = [0,1,2,3,4,5,6,7,8,9,10,11,12]
List2 = ['tret','jan','feb','mar','apr','may','jun','jly','aug','sep','oct','nov','dec']
List3 = ['','tam','hel','maa','huh','tou','kes','hei','elo','syy','lok','mer','jou']
MtEDict = {List2[i]:i for i in range(13)}
for j in range(1,13) :
    MtEDict[List3[j]]=j*13
def convert(num,rule=13) :
    if num < rule :
        print (List2[num])
    elif num % rule != 0 :
        print(List3[num // rule] + ' '+ List2[num % rule])  
    else :
        print(List3[num // rule])
def convert10(string) :
    res = 0
    numlist = string.split()
    for i in numlist :
        res += MtEDict[i]
    print(res) 

n = int(input())    
for i in range(n) :
    InPutString = input()
    if InPutString.isdigit() :
        convert(int(InPutString))
    else :
        convert10(InPutString)


