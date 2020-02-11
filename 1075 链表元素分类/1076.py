ad0,n,k = input().split()
n,k = int(n),int(k)
nodedict = {}
nodedict2 = {}
for i in range(n) :
    node = input().split()
    nodedict[node[0]] = (int(node[1]),node[2])

address = ad0
while address != '-1' :
    data = nodedict[address][0]
    if data < 0 :
        nodedict2[address] = [data,-1]
        if len(nodedict2) == 1 :
            ad1 = address
        else :
            nodedict2[last][1] = address
        last = address
    address = nodedict[address][1]
address = ad0
while address != '-1' :
    data = nodedict[address][0]
    if 0 <= data <= k :
        nodedict2[address] = [data,-1]
        if len(nodedict2) == 1 :
            ad1 = address
        else :
            nodedict2[last][1] = address
        last = address
    address = nodedict[address][1]
address = ad0
while address != '-1' :
    data = nodedict[address][0]
    if data > k :
        nodedict2[address] = [data,-1]
        if len(nodedict2) == 1 :
            ad1 = address
        else :
            nodedict2[last][1] = address
        last = address
    address = nodedict[address][1]
address = ad1

for i in nodedict2:
    print(address,nodedict2[address][0],nodedict2[address][1])
    address = nodedict2[address][1]


