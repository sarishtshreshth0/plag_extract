Q, H, S, D = map(int, input().split())
N = int(input())
Q1 = Q * 4
H1 = H * 2
D1 = D / 2
if min(Q1, H1, S) > D1:
  ans = D * (N // 2) + min(Q1, H1, S) * (N % 2)
else:
  ans = min(Q1, H1, S) * N
  
print(ans)