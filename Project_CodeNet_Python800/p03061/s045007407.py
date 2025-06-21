import sys
readline = sys.stdin.readline

N = int(readline())
A = list(map(int,readline().split()))

if N == 2:
  print(max(A))
  exit(0)

def gcd(a,b):
  if a < b:
    a,b = b,a
  while a%b > 0:
    a,b = b,a%b
  return b

left = [None] * N
left[0] = A[0]
for i in range(1, len(A)):
  left[i] = gcd(left[i - 1],A[i])

right = [None] * N
right[-1] = A[-1]
for i in range(len(A) - 2,-1,-1):
  right[i] = gcd(right[i + 1],A[i])

ans = max(left[-2],right[1])
for i in range(1, len(A) - 1):
  g = gcd(left[i - 1],right[i + 1])
  if ans < g:
    ans = g
print(ans)
