a,b=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    if i<0:
        i=-i
    d=str(i)
    if len(d)==b:
        c=c+1
print(c)