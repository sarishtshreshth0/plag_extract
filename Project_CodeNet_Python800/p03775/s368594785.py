N = int(input())

def cal_divisors(N):
    divisors = []
    i = 1
    while i*i <= N:
        if N % i == 0:
            divisors.append(i)
        i += 1
    return divisors

divisors = cal_divisors(N)
ans = 10**12

for d in divisors:
    ans = min(ans,max(len(str(d)),len(str(N//d))))
print(ans)