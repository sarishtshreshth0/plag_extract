n = int(input())
a1 = list(map(int, input().split()))
a2 = []
if n == 1:
    print(1)
else:
    for i in a1:
        a2.append(i)
        a2.append(i+1)
        a2.append(i-1)
    from collections import Counter
    a = Counter(a2).most_common()
    print(a[0][1])