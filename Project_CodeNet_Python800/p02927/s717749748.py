import sys

read = sys.stdin.read
M, D = map(int, read().split())

if D < 22:
    print(0)
    exit()

answer = 0
for i in range(1, M + 1):
    for j in map(str, range(22, D + 1)):
        a = int(j[0])
        b = int(j[1])
        if a >= 2 and b >= 2:
            if a * b == i:
                answer += 1

print(answer)
