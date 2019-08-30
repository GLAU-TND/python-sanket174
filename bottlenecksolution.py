'''c=int(input("enter the no.of element"))
a=list(map(int,input().split( )))
i=0
a.sort()
x = 0
a[1]=c
if c==(a[i]):
  for i in range(1):

       x=x+1
       print(x)
else:
       print(1)
'''



n=int(input("enter the no."))
res=list(map(int,input().split()))
lst=[]

for i in res:
    lst.append(res.count(i))

print(max(lst))

