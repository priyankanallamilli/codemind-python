import math
def is_prime(n):
    sq=int(math.sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
for i in range(int(input())):
    n=int(input())
    for k in range(n,0,-1):
        if is_prime(k):
            break
    for I in range(n,n*n):
        if is_prime(I):
            break
    a=n-k
    b=I-n
    if a<b:
        print(k)
    elif b<a:
        print(I)
    elif a==b:
        print(k)