N = int(input())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
A = sorted(A, key=lambda x: -x[1])  # sort by y-axis [max,..., min]
B = sorted(B, key=lambda x: x[0])   # sort by x-axis [min,..., max]

for i in range(N):
    for j in range(len(A)):
        if A[j][0] < B[i][0] and A[j][1] < B[i][1]:
            A.pop(j)
            break

print(N - len(A))
