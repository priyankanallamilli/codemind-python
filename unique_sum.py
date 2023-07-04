n=int(input())
lst=list(map(int,input().split()))
a=[]
for i in lst:
    if i not in a:
        a.append(i)
print(sum(a))