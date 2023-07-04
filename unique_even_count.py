n=int(input())
lst=list(map(int,input().split()))
e=[]
c=0
for i in lst:
    if i%2==0:
        e.append(i)
b=set(e)
for i in b:
    if i%2==0:
        c=c+1
print(c)