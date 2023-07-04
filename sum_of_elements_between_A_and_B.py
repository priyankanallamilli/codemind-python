n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
e=[]
flag=0
for i in lst:
    if i>=a and i<=b:
        flag=1
        e.append(i)
if flag==1:
    print(sum(e))