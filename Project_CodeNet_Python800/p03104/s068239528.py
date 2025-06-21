A, B = map(int, input().split())
ans = 0
if A % 2 == 0:
  if ((B + 1 - A) // 2) % 2 == 1:
    ans ^= 1
else:
  if ((B - A) // 2) % 2 == 1:
    ans ^= 1
  ans ^= A
if B % 2 == 0:
  ans ^= B
print(ans)