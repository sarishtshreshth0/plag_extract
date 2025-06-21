n = int(input())
w = list(map(int, input().split()))
diff_min = sum(w)
for i in range(len(w)):
    s1 = sum(w[:i + 1])
    s2 = sum(w[i + 1:])
    diff = abs(s1 - s2)
    if diff < diff_min:
        diff_min = diff
print(diff_min)