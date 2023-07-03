n=int(input())
lst=list(map(int,input().split()))
a=lst[::-1]
l=[]
for i in range(n):
    if lst[i]%2!=0:
        l.append(lst[i])
print(l[-1])