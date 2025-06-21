Q, H, S, D=map(int, input().split())
N=int(input())
one=min(4*Q, 2*H, S)

ans=min(one*N, D*(N//2)+one*(N%2))
print(ans)