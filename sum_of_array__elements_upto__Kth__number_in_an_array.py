n=int(input())
lst=list(map(int,input().split()))
k=int(input())
e=[]
for i in lst:
    if i<=k:
        e.append(i)
print(sum(e))