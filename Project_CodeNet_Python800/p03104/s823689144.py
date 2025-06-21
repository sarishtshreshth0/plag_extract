from math import ceil
A, B = map(int, input().split())
res = 0
if B-A+1<=20:
    for a in range(A,B+1):
        res^=a
    print(res)
    exit()
for a in range(A,ceil(A/4)*4):
    res ^= a
for b in range((B//4)*4,B+1):
    res ^= b
print(res)