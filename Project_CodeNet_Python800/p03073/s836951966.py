s = list(input())

a = ['1', '0']*10**5
b = ['0', '1']*10**5

A = a[:len(s)]
B = b[:len(s)]
cnt = 0
ans = 0
for i in range(len(s)):
    if s[i] != A[i]:
        cnt += 1
    if s[i] != B[i]:
        ans += 1
print(min(cnt, ans))