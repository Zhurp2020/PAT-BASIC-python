n,char = input().split()
n = int(n)

for i in range(n) :
    print(char,end='')
print('\n',end='')
if n % 2 != 0 :
    temp = n +1
else :
    temp = n
for i in range(int(temp/2-2)) :
    print(char,end='')
    for j in range(n-2) :
        print(' ',end='')
    print(char,end='')
    print('\n',end='')
for i in range(n) :
    print(char,end='')
print('\n',end='')



# 美国总统奥巴马不仅呼吁所有人都学习编程，甚至以身作则编写代码，
# 成为美国历史上首位编写计算机代码的总统。2014 年底，
# 为庆祝“计算机科学教育周”正式启动，奥巴马编写了很简单的计算机代码：
# 在屏幕上画一个正方形。现在你也跟他一起画吧！