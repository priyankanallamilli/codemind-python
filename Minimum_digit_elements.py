n=int(input())
l=list(map(int,input().split()))
c=0
min=999
for i in l:
    if len(str(i))<min:
        min=len(str(i))
for i in l:
    if min==len(str(i)):
        c+=1
print(c)
        