N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 0
now = A[0]
start_idx = 0
while now <= A[-1] + 1:
    tmp_max = 0
    flag = True
    for i in range(start_idx, N):
        if flag and now - 1 == A[i]:
            flag = False
            start_idx = i
        if now - 1 <= A[i] <= now + 1:
            tmp_max += 1
        if now + 1 < A[i]:
            break
    ans = max(tmp_max, ans)
    now += 1
print(ans)