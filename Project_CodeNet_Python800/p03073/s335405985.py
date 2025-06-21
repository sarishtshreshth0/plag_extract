s = list(input())
n = len(s)
a = ['0'] * n
b = ['0'] * n
for i in range(n):
    if i % 2 ==1:
        a[i] = '1'
    else:
        b[i] = '1'

cnt_a, cnt_b = 0, 0
for i in range(n):
    if s[i] != a[i]:
        cnt_a += 1
    if s[i] != b[i]:
        cnt_b += 1
print(min(cnt_a, cnt_b))