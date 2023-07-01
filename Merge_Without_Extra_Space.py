n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))
    e=lst1+lst2
    f=sorted(e)
    print(*f)