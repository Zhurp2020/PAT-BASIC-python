m,n,tol = list(map(int,input().split()))
image = []
colors = {}
for i in range(n) :
    if m == 1 :
        line = [int(input())]
    else:
        line = list(map(int,input().split()))
    image.append(line)
    for j in line :
        if j in colors :
            colors[j] += 1
        else :
            colors[j] = 1
count = 0

if m == n == 1 :
    print('(1, 1): {}'.format(image[0][0]))
    exit()
for i in range(n) :
    for j in range(m) :
        special = True
        if colors[image[i][j]] > 1 :
            continue
        if i == 0 :
            if j == 0 :
                surround = [            image[0][1],
                            image[1][0],image[1][1]]
            elif j == m-1:
                surround = [image[0][-2],
                            image[1][-2],image[1][-1]]
            else :
                surround = [image[0][j-1],            image[0][j+1],
                            image[1][j-1],image[1][j],image[1][j+1]]
        elif  i == n -1:
            if j == 0 :
                surround = [image[-2][0],image[-2][1],
                                         image[-1][1]]
            elif j == m-1:
                surround = [image[-2][-2],image[-2][-2],
                            image[-1][-2]              ]
            else:
                surround = [image[-2][j-1],image[-2][j],image[-2][j+1],
                            image[-1][j-1],             image[-1][j+1]]
        else:
            if j == 0 :
                surround = [image[i-1][0],image[i-1][1],
                                          image[i][1]  ,
                            image[i+1][0],image[i+1][1]]
            elif j == m-1 :
                surround = [image[i-1][-2],image[i-1][-1],
                            image[i][-2]                 ,
                            image[i+1][-2],image[i+1][-1]]
            else:
                surround = [image[i-1][j-1],image[i-1][j],image[i-1][j+1],
                            image[i][j-1]  ,              image[i][j+1]  ,
                            image[i+1][j-1],image[i+1][j],image[i+1][j+1]]
        for k in surround :
            if abs(k-image[i][j]) <= tol :
                special = False               
                break
        if special :
            count += 1
            x,y = j+1,i+1
            color = image [i][j]
        if count == 2 :
            break

if count == 0 :
    print('Not Exist')
if count == 1 :
    print('({}, {}): {}'.format(x,y,color))
if count == 2 :
    print('Not Unique')

