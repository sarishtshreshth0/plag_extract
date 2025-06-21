def solve():
  Q, H, S, D = map(int, input().split())
  N = int(input())
  two = min([Q*8,H*4,S*2,D])
  one = min([Q*4,H*2,S])
  ans = two*(N//2)+one*(N%2)
  return ans
print(solve())