n=int(input())
lst=list(map(int,input().split()))
c=0
a=[]
for i in lst:
    if i not in a:
        a.append(i)
for i in a:
    if i%2!=0:
        c=c+1
print(c)