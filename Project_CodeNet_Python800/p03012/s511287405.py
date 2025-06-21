N = int(input())
W = [int(i) for i in input().split()]

ans = sum(W)
s = ans
t = 0
for i in W:
  s -= i
  t += i
  ans = min(abs(s-t), ans)
  
print(ans)