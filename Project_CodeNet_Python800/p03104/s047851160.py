a,b = map(int,input().split())
def cal(n):
  if n % 4 == 1:
    return 1
  if n % 4 == 3:
    return 0
  if n % 4 ==2:
    return n + 1
  else:
    return n
  
print(cal(a-1) ^ cal(b))