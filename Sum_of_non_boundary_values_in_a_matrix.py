r,c=map(int,input().split())
mat=[]
for i in range(r):
    lst=list(map(int,input().split()))
    mat.append(lst)
a=[]
for i in range(1,r-1):
    for j in range(1,c-1):
        a.append(mat[i][j])
print(sum(a))