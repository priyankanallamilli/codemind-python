r,c=map(int,input().split())
mat=[]
for i in range(r):
    lst=list(map(int,input().split()))
    mat.append(lst)
esum=[]
osum=[]
for i in range(r):
    if i%2==0:
        esum.append(sum(mat[i]))
    else:
        osum.append(sum(mat[i]))
print(sum(esum),sum(osum))