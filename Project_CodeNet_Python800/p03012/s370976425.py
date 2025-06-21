N = int(input())
W = list(map(int, input().split()))
w_sum = sum(W)

val_sum = 0
val_diff = w_sum
for i in range(N):
    val_sum += W[i]
    diff = abs(2 * val_sum - w_sum)
    if diff < val_diff:
        val_diff = diff
    else:
        break

print(val_diff)