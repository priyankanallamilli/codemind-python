n=int(input())
lst=list(map(int,input().split()))
b=n//2
a=lst[:b]
c=lst[b:]
d=sum(a)
e=sum(c)
print(e-d)