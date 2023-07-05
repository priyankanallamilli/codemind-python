a,b=map(int,input().split())
lst=list(map(int,input().split()))
lst1=list(map(int,input().split()))
e=[]
for i in lst:
    if i in lst1:
        e.append(i)
a=[]
for i in e:
    if i not in a:
        a.append(i)
print(*a)
