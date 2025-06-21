A,B = map(int,input().split())
dif = B-A+1
MAX = 45
ans = 0
for i in range(1,MAX):
  base = pow(2,i)
  if (B+1)%base <= base//2:
    up = ((B+1)//base)*(base//2)
  else:
    up = ((B+1)//base)*(base//2) + (B+1)%base - base//2
  if A%base <= base//2:
    down = (A//base)*(base//2)
  else:
    down = (A//base)*(base//2) + A%base - base//2
  ans += (up-down)%2*(base//2)
print(ans)
