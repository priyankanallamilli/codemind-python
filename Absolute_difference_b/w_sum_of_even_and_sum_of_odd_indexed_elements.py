n=int(input())
lst=list(map(int,input().split()))
e=0
o=0
for i in range(len(lst)):
    if i%2==0:
        e=e+lst[i]
    else:
        o=o+lst[i]
a=e-o
print(a)