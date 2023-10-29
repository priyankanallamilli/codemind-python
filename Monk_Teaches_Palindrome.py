n=int(input())
for i in range(n):
    a=input()
    b=len(a)
    c=int(b)
    if a==a[::-1] and c%2==0:
        print("YES EVEN")
    elif a==a[::-1] and c%2!=0:
        print("YES ODD")
    else:
        print("NO")