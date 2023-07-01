n=int(input())
d=list(map(int,input().split()))
a=n//2
c=d[a:]
b=d[:a]
e=c[::-1]
print(*e,*b)