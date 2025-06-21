N = int(input())
A = input().split()
S = [0] * (N + 1)

for i in range(N):
    S[i + 1] = S[i] + int(A[i])

S.sort()
zero = 0
same_number = 0
for i in range(1,N + 1):
    if S[i] == S[i-1]:
        same_number += 1
    else:
        if same_number > 0:
            zero = zero + ((same_number * (same_number + 1)) / 2)
        same_number = 0

if same_number > 0:
    zero = zero + (same_number * (same_number + 1) / 2)

print(int(zero))