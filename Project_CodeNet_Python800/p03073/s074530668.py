S = list(input())

odd0, odd1 = 0, 0
even0, even1 = 0, 0
for i, s in enumerate(S):
    if i % 2 == 0:
        if s == "0":
            even0 += 1
        else:
            even1 += 1
    else:
        if s == "0":
            odd0 += 1
        else:
            odd1 += 1
print(min(even0+odd1, even1+odd0))



