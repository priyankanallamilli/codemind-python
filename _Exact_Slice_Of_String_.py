n=input()
a=int(input())
b=int(input())
l=[]
for i in range(a,b+1):
    l.append(n[i])
l="".join(l)
print(l)