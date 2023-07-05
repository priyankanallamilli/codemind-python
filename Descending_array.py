n=int(input())
lst=list(map(int,input().split()))
b=set(lst)
a=sorted(b)
c=a[::-1]
if c==lst:
    print("yes")
else:
    print("no")