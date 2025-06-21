n = int(input())
A = list(map(int, input().split()))
C = [0] * 100002
for x in A:
    for i in range(3):
        C[x + i] += 1
print(max(C))