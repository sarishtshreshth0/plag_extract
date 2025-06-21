n, k = map(int, input().split())

s = ""
while(True):
  if n < k :
    s += str(n)
    break
  else :
    s += str(n%k)
    n = n//k

print(len(s))