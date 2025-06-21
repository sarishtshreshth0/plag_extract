n = int(input())
red = []
blue = []

for i in range(n):
    a, b = map(int, input().split())
    red.append((a, b))

for i in range(n):
    a, b = map(int, input().split())
    blue.append((a, b))

red.sort(key=lambda x:x[1], reverse=True)
blue.sort()
chk = [False] * n

for b in blue:
    for i, r in enumerate(red):
        if chk[i]:
            continue
        elif r[0] < b[0] and r[1] < b[1]:
            chk[i] = True
            break
print(sum(chk))
