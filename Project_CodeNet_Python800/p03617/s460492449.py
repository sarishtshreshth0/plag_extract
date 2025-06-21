Q,H,S,D=map(int,input().split(' '))
N = int(input())
l1 = min(4*Q,2*H,S)
l2 = min(2*l1,D)
if N==1:
    print(l1)
elif N%2==0:
    print(N//2*l2)
else:
    print(N//2*l2+l1)