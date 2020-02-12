n,m = [int(i) for i in input().split()]

for i in range(n) :
    scorelist = [int(i) for i in input().split()]
    g1 = scorelist[0]
    rightlist = []
    for j in scorelist[1:] :
        if 0 <= j <= m :
            rightlist.append(j)
    rightlist.remove(max(rightlist))
    rightlist.remove(min(rightlist))
    g2 = sum(rightlist)/len(rightlist)
    final = (g1+g2)/2
    if abs(int(final) - final) >= 0.5:
        final = int(final+1)
    print(int(final))