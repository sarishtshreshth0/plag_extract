def from_10_to_n(x, n):
  tmp = x
  out = ''
  while tmp > 0:
    out = str(x % n) + out
    tmp = tmp // n
  return out
 
N, K = map(int, input().split())
N = from_10_to_n(N, K)
print(len(N))