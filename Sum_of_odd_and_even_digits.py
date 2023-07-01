n=int(input())
lst=list(map(int,input().split()))
e=0
o=0
for i in range(n):
    if i%2==0:
        e=e+lst[i]
    else:
        o=o+lst[i]
if(o-e==0):
    print("YES")
else:
    print("NO")