Q, H, S, D = map(int, input().split())
N = int(input())
l = min(4*Q, 2*H, S)
if 2*l > D:
  print(D*(N//2) + N%2 * l)
else:
  print(l*N)