r=int(input())
c=int(input())
mat=[]
for i in range(r):
    lst=list(map(int,input().split()))
    mat.append(lst)
rsum=[]
for i in range(r):
    rsum.append(sum(mat[i]))
print(sum(rsum))