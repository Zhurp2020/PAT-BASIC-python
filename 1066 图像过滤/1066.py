m,n,low,high,target = list(map(int,input().split()))
image = []
for i in range(m) :
    image.append(input().split())

for i in range(m) :
    for j in range(n) :
        image[i][j] = image[i][j].rjust(3,'0')
        if low <= int(image[i][j]) <= high :
            image[i][j] = str(target).rjust(3,'0')
    print(' '.join(image[i]))
