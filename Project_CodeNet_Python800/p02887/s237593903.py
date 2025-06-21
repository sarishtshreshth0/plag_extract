n = int(input())
s = input()
sl = list(s)
k = 0
cur = '0'
for i in range(n):
    if sl[i] == cur:
        continue
    else:
        k += 1
        cur = sl[i]
print(k)