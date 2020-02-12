CorD = input()
stringin = input()

def compress(string) :
    res = ''
    i = 0
    while i <= len(string) -1 :
        count = 1
        while i <= len(string) -2 and string[i] == string[i+1]:
            count += 1
            i += 1
        if count > 1 :
            res += str(count) + string[i]
        else :
            res += string[i]
        i += 1
    return res 
def decompress(string):
    res = ''
    i = 0
    while i <= len(string) -1 :
        if string[i].isdigit():
            number = string[i]
            while string[i+1].isdigit() :
                number += string[i+1]
                i += 1
            res += int(number) * string[i+1]
            i += 2
        else:
            res += string[i]
            i += 1
    return res

if CorD == 'C':
    print(compress(stringin))
else:
    print(decompress(stringin))