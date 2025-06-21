import itertools
n = int(input())
cnt = 0
for i in range(3,len(str(n))+1):
    for v in itertools.product(["3","5","7"], repeat=i):
        if len(set(v))!=3: continue
        x = int("".join(v))
        if n >= x: cnt += 1

print(cnt)