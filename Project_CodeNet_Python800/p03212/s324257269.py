N=int(input())
P=0
def f(x):
  global N,P
  if x>N:
    return None
  s=str(x)
  if '7' in s and '5' in s and '3' in s:
    P+=1
  f(x*10+7)
  f(x*10+5)
  f(x*10+3)
f(7)
f(5)
f(3)
print(P)