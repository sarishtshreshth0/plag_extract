import sys

N = int(input())
CSF = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(N - 1)]

for i in range(N - 1):
    res = 0
    for c, s, f in CSF[i:]:
        if res < s:
            res = s + c
        elif res % f == 0:
            res += c
        else:
            res += f - (res % f) + c
    print(res)
print(0)
