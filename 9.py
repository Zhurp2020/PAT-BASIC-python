n = input()
countspace = 0
words = []
for char in n :
    if char == ' ' :
        countspace = countspace + 1
words [:countspace+1] = n.split()

for i in words[len(words):0:-1] :
   print(i,end= ' ')
print(words[0])


# 给定一句英语，要求你编写程序，将句中所有单词的顺序颠倒输出。