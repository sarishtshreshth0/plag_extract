s = list(input())
n = len(s)-1
a = [1]+[0]*n
b = [0]+[1]*n
difA = 0
difB = 0

for i in range(1,n+1):
    a[i] = 0 if a[i-1] == 1 else 1
    b[i] = 0 if b[i-1] == 1 else 1

for j in range(n+1):
    if a[j] != int(s[j]):
        difA += 1
    if b[j] != int(s[j]):
        difB += 1

ans = min(difA,difB)

print(ans)