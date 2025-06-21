n = int(input())
RED, BLUE = [], []
for _ in range(n):
    RED.append(tuple(map(int, input().split())))
for _ in range(n):
    BLUE.append(tuple(map(int, input().split())))

RED = sorted(RED, key=lambda x: x[0], reverse=True)

count = 0
for r in RED:
    for b in sorted(BLUE, key=lambda x: x[1]):
        if r[0] <= b[0] and r[1] <= b[1]:
            BLUE.remove(b)
            count += 1
            break
    
print(count)