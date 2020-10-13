a = input()
b = input()
Broken= ''

for i in a :
    if not(i in b) and not (i.upper() in Broken):
        Broken += i.upper()      

print(Broken)



# 旧键盘上坏了几个键，于是在敲一段文字的时候，对应的字符就不会出现。
# 现在给出应该输入的一段文字、以及实际被输入的文字，
# 请你列出肯定坏掉的那些键。