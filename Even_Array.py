n=int(input())
lst=list(map(int,input().split()))
a=[]
for i in range(n):
    if lst[i]%2==0:
        a.append(i)
if len(a)==n:
    print("True")
else:
    print("False")