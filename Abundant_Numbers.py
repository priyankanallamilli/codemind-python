n=int(input())
e=[]
for i in range(1,n):
    if n%i==0:
        e.append(i)
if sum(e)>=n:
    print("True")
else:
    print("False")