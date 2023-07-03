n=int(input())
lst=list(map(int,input().split()))
e=0
e1=0
for i in lst:
    if i%2==0:
        e+=i
    else:
        e1+=i
if e>e1:
    print(e-e1)
else:
    print(e1-e)