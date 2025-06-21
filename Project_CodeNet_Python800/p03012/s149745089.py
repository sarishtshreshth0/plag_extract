n = int(input())
w = [int(e) for e in input().split(" ")]
w_sum = sum(w)
s_diff = []
s1 = 0
s2 = w_sum
for i in range(n+1):
    s_diff.append(abs(s2 - s1))
    if (i == n):
        break
    s1 += w[i]
    s2 -= w[i]

print(min(s_diff))
