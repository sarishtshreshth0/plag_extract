import sys
input = sys.stdin.readline

cnt = 0
m,d = map(int, input().split())
for i in range(1, m+1):
        for j in range(11, d+1):
                d1 = j//10
                d2 = j%10
                if d1 * d2 == i and d1>1 and d2 > 1:
                        cnt += 1
print(cnt)
