n=int(input())
lst=list(map(int,input().split()))
for i in lst:
    if i<0:
        i=-i
    d=str(i)
    print(len(d),end=" ")