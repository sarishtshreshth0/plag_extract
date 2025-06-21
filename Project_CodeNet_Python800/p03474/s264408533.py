A, B = map(int, input().split())
S = input()
ans = True
if S[A] != '-':
    ans = False
for i in range(len(S)):
    if i == A:
        continue
    if S[i] == '-':
        ans = False
if ans:
    print('Yes')
else:
    print('No')