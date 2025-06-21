N = int(input())
ans = len(str(10**10))
for a in range(1, int(N**0.5)+1):
    d, r = divmod(N, a)
    if r==0:
        l = max([len(str(n)) for n in [d, a]])
        ans = min(ans, l)
print(ans)
