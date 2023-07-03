n=int(input())
lst=list(map(int,input().split()))
a=len(lst)
b=sum(lst)
c=b/a
d=format(c,".2f")
print(d)