n,k = map(int,input().split())
def base10to(n, k):
  if(int(n/k)):
    return base10to(int(n/k), k) + str(n%k)
  return str(n%k)
print(len(base10to(n,k)))