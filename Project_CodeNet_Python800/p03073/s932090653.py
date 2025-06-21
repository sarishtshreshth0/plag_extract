s = list(input())
n = len(s)
a = ['1']+['0']*(n-1)
b = ['0']+['1']*(n-1)

for i in range(1,n):
    if a[i-1] == '1':
        a[i] = '0'
    elif a[i-1] == '0':
        a[i] = '1'

    if b[i-1] == '1':
        b[i] = '0'
    elif b[i-1] == '0':
        b[i] = '1'

difA = 0
difB = 0

for j in range(n):
    if a[j] != s[j]:
        difA += 1

    if b[j] != s[j]:
        difB += 1

ans = min(difA,difB)

print(ans)