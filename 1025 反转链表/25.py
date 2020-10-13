a,n,k = input().split()
nodesdict = {}
nodeslist = []
newnodeslist = []
n,k = list(map(int,[n,k]))
for i in range(n) :
    address,data,nextad = input().split()
    nodesdict[address] = (data,nextad)

for i in range(n) :
    nodeslist.append((a,nodesdict[a]))
    a = nodesdict[a][1]
for i in range(n // k) :
    for j in range(k) :
        newnodeslist.append(nodeslist[(i+1)*k-(j+1)])
for i in range(n % k) :
    newnodeslist.append(nodeslist[(n//k)*k + i])

for i in range(n-1) :
    print(newnodeslist[i][0],newnodeslist[i][1][0],newnodeslist[i+1][0])
print(newnodeslist[-1][0],newnodeslist[-1][1][0],'-1')




#def printLink(link,k,addNode):
#    data=[]
#    ls=[]
#    while addNode!='-1':
#        subData=[]
#        subLink=[]
#        for i in range(k):
#            if addNode!='-1':
#                subData.append(link.get(addNode))
#                subLink.append(addNode)
#                addNode=subData[i][2]
#            else:
#                subData.reverse()
#                subLink.reverse()
#                break
#        subData.reverse()
#        subLink.reverse()
#        data+=subData
#        ls+=subLink
#    ls.append('-1')
#    for i in range(len(data)):
#        print('{} {} {}'.format(data[i][0],data[i][1],ls[i+1]))
#addNode,n,k=input().split()
#k=eval(k)
#link={}
#for i in range(eval(n)):
#    addr,data,nextAddr=input().split()
#    link[addr]=(addr,data,nextAddr)
#printLink(link,k,addNode)



# 给定一个常数 K 以及一个单链表 L，
# 请编写程序将 L 中每 K 个结点反转。
# 例如：给定 L 为 1→2→3→4→5→6，K 为 3，
# 则输出应该为 3→2→1→6→5→4；如果 K 为 4，
# 则输出应该为 4→3→2→1→5→6，即最后不到 K 个元素不反转。