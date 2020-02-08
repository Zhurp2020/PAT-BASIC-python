tokens,k = [int(i) for i in input().split()]

for i in range(k) :
    n1,b,t,n2 = [int(i) for i in input().split()]
    if t > tokens :
        print('Not enough tokens.  Total = {}.'.format(tokens))
    else :
        if (b == 0 and n2 < n1) or (b == 1 and n2 > n1):
            tokens += t
            print('Win {}!  Total = {}.'.format(t,tokens))
        else :
            tokens -= t
            print('Lose {}.  Total = {}.'.format(t,tokens))
    if tokens <= 0 :
        print('Game Over.')
        break