n =int(input())
person = []
count = 0
for i in range(n) :
    man = input().split()
    if '1814/09/06' <= man[1] <= '2014/09/06' :
        count += 1
        person.append(man)

if count > 0 :
    max = [person[0][0],person[0][1]]
    min = [person[0][0],person[0][1]]
    for i in person :
        if i[1] < max[1] :
            max = i
        if i[1] > min[1] :
            min = i
    print(count,max[0],min[0])
else :
    print('0')



# 某城镇进行人口普查，得到了全体居民的生日。现请你写个程序，
# 找出镇上最年长和最年轻的人。
# 这里确保每个输入的日期都是合法的，但不一定是合理的——
# 假设已知镇上没有超过 200 岁的老人，而今天是 2014 年 9 月 6 日，
# 所以超过 200 岁的生日和未出生的生日都是不合理的，应该被过滤掉。