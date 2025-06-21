def check(n):
    min_len = 1 << 60
    for i in range(1, int(n**.5 + 1)):
        if n % i == 0:
            a= i
            b= n//i
            min_len = min(min_len, max(len(str(a)), len(str(b))))
    return min_len


n = int(input())
res = check(n)
print(res)