n=int(input())
lst=list(map(int,input().split()))
a=sorted(lst)
b=[]
c=0
for i in a:
    c=i*i
    b.append(c)
d=sorted(b)
print(*d)