r,c=map(int,input().split())
mat=[]
for i in range(r):
    lst=list(map(int,input().split()))
    mat.append(lst)
b=0
for i in range(1,r-1):
    for j in range(1,c-1):
        b=b+mat[i][j]
e=0
for i in range(r):
    for j in range(c):
        e=e+mat[i][j]
print(e-b)