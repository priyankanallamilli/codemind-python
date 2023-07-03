r,c=map(int,input().split())
mat=[]
for i in range(r):
    lst=list(map(int,input().split()))
    mat.append(lst)
c=0
for i in range(r):
    k=sorted(mat[i])
    if mat[i]==k or mat[i]==k[::-1]:
        c+=1
print(c)
        