ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()
if n%2==0:
  print(n)
else:
  print(2*n)