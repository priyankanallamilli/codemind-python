n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
e=[]
flag=0
for i in lst:
    if i<a or i>b:
        flag=1
        e.append(i)
        d=min(e)
if flag==1:
    print(d)
else:
    print(-1)