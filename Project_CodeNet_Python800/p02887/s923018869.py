N = int(input())
S = input()
now = -1
for s in S:
    if now == s:
        N -=1
    now = s
print(N)