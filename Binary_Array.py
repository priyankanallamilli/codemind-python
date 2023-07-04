n=int(input())
lst=list(map(int,input().split()))
a=[]
for i in range(n):
    if i not in a:
        a.append(i)
c=0
for i in range(n):
    if lst[i]==0 or lst[i]==1:
        c=c+1
if c==len(lst):
    print("True")
else:
    print("False")