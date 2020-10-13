broken = input()
InputString = input()
res = ''
shiftbroken = False

if '+' in broken :
    shiftbroken = True
for i in InputString :
    check = i.upper()
    if check in broken or (i.isupper() and shiftbroken):
        continue
    else :
        res = res + i

print(res) 



# 旧键盘上坏了几个键，于是在敲一段文字的时候，对应的字符就不会出现。
# 现在给出应该输入的一段文字、以及坏掉的那些键，打出的结果文字会是怎样？