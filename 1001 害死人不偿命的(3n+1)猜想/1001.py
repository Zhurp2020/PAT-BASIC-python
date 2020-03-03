n = int(input())
count = 0
def calc(a):
   if a % 2 == 1 :
      return (3 * a + 1) / 2
   else :
      return a/2

while n != 1 :
   n = calc(n)
   count += + 1

print (count)


