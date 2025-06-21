a,b=map(int, input().split())

if a == 1 or b == 1:
    print(1)
if a != 1 and b != 1 and a*b%2== 0:
    print(a*b//2)
if a != 1 and b != 1 and a*b%2!= 0:
    print(a*b//2+1)