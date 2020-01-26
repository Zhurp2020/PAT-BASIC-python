n = int(input())
IdNums = []
for i in range(n) :
    IdNums.append(input())
flag = 0
def CheckId (Id):
    z = 0
    if not(Id[0:17].isdigit()) :
        return False
    else :
        QuanZhong = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
        M= [1,0,'X',9,8,7,6,5,4,3,2]
        for i in range(17) :
            z = QuanZhong[i] * int(Id[i]) +z 
        z = z % 11
        if Id[17] == str(M[z]) :
            return True
        else :
            return False

for i in IdNums :
    if not(CheckId(i)) :
        print(i)
        flag = 1
if flag == 0 :
    print('All passed')



# 一个合法的身份证号码由17位地区、日期编号和顺序编号加1位校验码组成。
# 校验码的计算规则如下：
# 首先对前17位数字加权求和，权重分配为：
# {7，9，10，5，8，4，2，1，6，3，7，9，10，5，8，4，2}；
# 然后将计算的和对11取模得到值Z；最后按照以下关系对应Z值与校验码M的值：
# Z：0 1 2 3 4 5 6 7 8 9 10
# M：1 0 X 9 8 7 6 5 4 3 2    
# 现在给定一些身份证号码，请你验证校验码的有效性，并输出有问题的号码。