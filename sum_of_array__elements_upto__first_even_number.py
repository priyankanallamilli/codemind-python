n=int(input())
lst=list(map(int,input().split()))
e=0
for i in lst:
    if i%2==0:
        break
    else:
        e=e+i
print(e)
    