def solve():
  X = int(input())
  ans = X//500*1000+(X%500)//5*5
  return ans
print(solve())