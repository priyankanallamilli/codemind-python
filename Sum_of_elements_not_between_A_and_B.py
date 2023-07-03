n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
for i in lst:
    if i<a or i>b:
        c=c+i
print(c)