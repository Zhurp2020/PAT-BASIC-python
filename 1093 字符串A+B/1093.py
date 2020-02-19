a = input()
b = input()

res = ''
for i in a :
    if not i in res :
        res += i
for i in b :
    if not i in res :
        res += i

print(res)