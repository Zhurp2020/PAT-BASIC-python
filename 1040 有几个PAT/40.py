patstring = input()
count = 0
long = len(patstring)
i = 0

for i in range(long) :
    if patstring[i] == 'P' :
        for j in range(i,long) :
            if patstring[j] == 'A' :
                for k in range(j,long) :
                    if patstring[k] == 'T' :
                        count += 1
       

print(count)



# n = input()
# count_P = count_PA = count_PAT = 0
# for i in n:
#     if 'P' == i:
#         count_P += 1
#     elif 'A' == i:
#         count_PA += count_P
#     else:
#         count_PAT += count_PA
# print(count_PAT % 1000000007)



# 字符串 APPAPT 中包含了两个单词 PAT，其中第一个 PAT 是第 2 位(P)，
# 第 4 位(A)，第 6 位(T)；第二个 PAT 是第 3 位(P)，第 4 位(A)，
# 第 6 位(T)。现给定字符串，问一共可以形成多少个 PAT？