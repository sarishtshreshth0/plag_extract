N = int(input())
S = input()

cnt = 1
last = S[0]
for s in S:
    if last == s:
        continue
    else:
        cnt += 1
        last = s
print(cnt)