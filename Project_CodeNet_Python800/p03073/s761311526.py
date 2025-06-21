S = input()
ans = 0
a = S[0]
for i in range(1, len(S)):
    if S[i] == a:
        ans += 1
    if a == '0':
        a = '1'
    else:
        a = '0'
print(ans)
