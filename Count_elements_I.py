a,b=map(int,input().split())
lst=list(map(int,input().split()))
lst1=list(map(int,input().split()))
e=[]
for i in lst:
    if i in lst1:
        e.append(i)
for i in lst1:
    if i in lst:
        e.append(i)
a=set(e)
print(len(a))
