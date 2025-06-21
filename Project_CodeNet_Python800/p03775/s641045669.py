def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

N = int(input())
A = make_divisors(N)
ans = float("inf")
#print(A)
if len(A)%2 == 0:
  mid = len(A)//2
else:
  mid = len(A)//2 + 1
for i in range(mid):
  temp = max(len(str(A[i])),len(str(A[-1-i])))
  ans = min(ans,temp)
print(ans)
  
