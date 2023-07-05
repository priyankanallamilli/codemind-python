n=int(input())
lst=list(map(int,input().split()))
b=set(lst)
a=sorted(b)
if a==lst:
    print("yes")
else:
    print("no")