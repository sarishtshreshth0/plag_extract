import math

def d_len(x):
  return len(str(x))

n=int(input())
rt=int(math.sqrt(n))
min_ab=10**10
for a in range (1,rt+1):
  if n % a !=0:
    continue
  b=n//a
  f_ab=max(d_len(a),d_len(b))
  min_ab=min(min_ab,f_ab)
print(min_ab)