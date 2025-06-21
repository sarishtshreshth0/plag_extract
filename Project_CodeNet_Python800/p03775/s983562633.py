def handan(a,b):
  return max(len(str(a)),len(str(b)))
def yakusu(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
N=int(input())
L=yakusu(N)
maxa=10**10
for i in range(len(L)):
  s=L[i]
  t=N//s
  maxa=min(maxa,handan(s,t))
print(maxa)