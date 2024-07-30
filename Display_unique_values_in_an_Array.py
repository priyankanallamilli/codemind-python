n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
arr=[k for k,v in d.items() if v==1]
if not arr:
    print("-1")
else:
    print(*arr)