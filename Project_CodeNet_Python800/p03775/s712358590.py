def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


x=int(input())
ans=float('inf')

for i in make_divisors(x):
  a,b=i,x//i
  a,b=str(a),str(b)

  ans=min(ans,max(len(a),len(b)))


print(ans)
