n=int(input())
lst=list(map(int,input().split()))
a=sum(lst)
b=a//n
if b in lst:
    print("True")
else:
    print("False")
