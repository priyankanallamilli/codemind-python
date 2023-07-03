r,c=map(int,input().split())
mat=[]
for i in range(r):
    lst=list(map(int,input().split()))
    mat.append(lst)
esum=0
osum=0
for i in range(r):
    for j in range(c):
        if mat[i][j]%2==0:
            esum=esum+mat[i][j]
        else:
            osum=osum+mat[i][j]
print(esum,osum)