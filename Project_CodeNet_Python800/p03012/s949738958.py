n = int(input())
w = list(map(int, input().split()))

s1 = 0
s2 = sum(w)
min_diff = s2

for x in w:
    x2 = x * 2
    if min_diff < x2:
        min_diff = min(x2 - min_diff, min_diff)
        break       
    min_diff -= x2
print(min_diff)
