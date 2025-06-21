from collections import defaultdict
n = int(input())
a_list = [int(x) for x in input().split()]
d = defaultdict(int)
for a in a_list:
    for i in range(-1, 2):
        d[a + i] += 1
print(sorted(d.values())[-1])