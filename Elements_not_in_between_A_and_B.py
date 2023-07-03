n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
flag=0
for i in lst:
    if i<a or i>b:
        flag=1
        c.append(i)
if flag==1:
    print(*c)
else:
    print(-1)