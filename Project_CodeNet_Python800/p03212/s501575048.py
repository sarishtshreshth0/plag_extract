import itertools

n = input()
ans = 0
l = ["3", "5", "7"]

for i in range(3, len(n) + 1):
    for j in itertools.product(l, repeat = i):
        j = "".join(j)
        if int(j) <= int(n):
            if "3" in str(j):
                if "5" in str(j):
                    if "7" in str(j):
                        ans += 1
print(ans)