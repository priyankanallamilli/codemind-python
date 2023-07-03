n=int(input())
lst=list(map(int,input().split()))
a=sum(lst)
avg=a/n
c=0
for i in range(n):
    if lst[i]<=avg:
        c=c+1
print(c)