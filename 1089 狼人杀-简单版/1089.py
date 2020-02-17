n = int(input())
playerlist = []
for i in range(1,n+1) :
    playerlist.append(int(input()))

for i in range(1,n) :
    for j in range(i+1,n+1):
        badliar = goodliar = 0 
        for k in range(1,n+1) :            
            if playerlist[k-1] <0 and abs(playerlist[k-1]) != i and abs(playerlist[k-1]) != j :
                if k == i or k == j :
                    badliar += 1
                else :
                    goodliar += 1
            elif playerlist[k-1] > 0 and (abs(playerlist[k-1]) == i or abs(playerlist[k-1]) == j):
                if k == i or k == j :
                    badliar += 1
                else :
                    goodliar += 1    
        if goodliar == badliar == 1 :
            print(i,j)
            exit()

print('No Solution')