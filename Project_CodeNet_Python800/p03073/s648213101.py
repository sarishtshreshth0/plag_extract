S = input()

first_0 = 0
first_1 = 0

for i, s in enumerate(S):
    if i % 2 == 0:
        if s == "0":
            first_1 += 1
        else:
            first_0 += 1
    else:
        if s == "0":
            first_0 += 1
        else:
            first_1 += 1

print(min(first_0, first_1))