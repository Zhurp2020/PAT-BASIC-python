tobuy = input()
wantbuy = input()
def countpearl(stringin) :
    resdict = {i:0 for i in stringin}
    for i in stringin :
        resdict[i] += 1
    return resdict
count = 0

tobuydict,wantbuydict = countpearl(tobuy),countpearl(wantbuy)
for i in wantbuydict :
    if not(i in tobuydict) :
        count += wantbuydict[i]
    elif wantbuydict[i] > tobuydict[i] :
        count += wantbuydict[i] - tobuydict[i]

if count == 0 :
    print('Yes',len(tobuy)-len(wantbuy))
else :
    print('No',count)



# 小红想买些珠子做一串自己喜欢的珠串。卖珠子的摊主有很多串五颜六色的珠串，
# 但是不肯把任何一串拆散了卖。于是小红要你帮忙判断一下，
# 某串珠子里是否包含了全部自己想要的珠子？如果是，
# 那么告诉她有多少多余的珠子；如果不是，那么告诉她缺了多少珠子。
# 为方便起见，我们用[0-9]、[a-z]、[A-Z]范围内的字符来表示颜色。
# 例如在图1中，第3串是小红想做的珠串；那么第1串可以买，
# 因为包含了全部她想要的珠子，还多了8颗不需要的珠子；第2串不能买，
# 因为没有黑色珠子，并且少了一颗红色的珠子。