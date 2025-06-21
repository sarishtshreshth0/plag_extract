Q,H,S,D=map(int,input().split())
N=int(input())
Min1=min(4*Q,2*H,S)
Min2=min(2*Min1,D)
Even=N//2
Odd=N%2
ans=Even*Min2+Odd*Min1
print(ans)