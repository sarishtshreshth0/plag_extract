n = int(input())
red = [[int(i) for i in input().split()] for _ in range(n)]
blue = [[int(i) for i in input().split()] for _ in range(n)]

red.sort(key=lambda x: x[1])
blue.sort()
is_paird = [0] * n
cnt = 0

for b in blue:
    idx = -1
    for i, r in enumerate(red):
        if not is_paird[i] and r[0] < b[0] and r[1] < b[1]:
            idx = i
    if idx != -1:
        is_paird[idx] = 1
        cnt += 1

print(cnt)
