from operator import itemgetter


n = int(input())
red = {tuple(int(i) for i in input().split()): False for _ in range(n)}
blue = {tuple(int(i) for i in input().split()): False for _ in range(n)}
c = 0
for b in sorted(blue.keys()):
    for r in sorted(red.keys(), key=itemgetter(1), reverse=True):
        if not red[r] and b[0] > r[0] and b[1] > r[1]:
            red[r] = True
            blue[b] = True
            c += 1
            break
print(c)
