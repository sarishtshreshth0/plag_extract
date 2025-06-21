N = int(input())
w = list(map(int, input().split()))
val0, val1 = 0, sum(w)
diff = val1

for i in range(N):
    val0 += w[i]
    val1 -= w[i]
    if diff <= abs(val1 - val0):
        print(diff)
        break
    else:
        diff = abs(val1 - val0)
