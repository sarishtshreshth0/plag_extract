Q,H,S,D=map(int,input().split())
N=int(input())

r1=[4*Q,2*H,S,D/2]

if N%2==0:
    print(round(min(r1)*2)*N//2)
else:
    if r1.index(min(r1))<=2:
        print(round(min(r1)*N))
    else:
        print(N//2*D+min(r1[:3]))