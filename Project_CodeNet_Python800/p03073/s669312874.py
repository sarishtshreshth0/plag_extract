n = input()
num = len(n)
one_s = 0
zero_s = 0

for i in range(num):
    if i % 2 == 0:
        if n[i] == "0":
            one_s += 1
        else:
            zero_s += 1
    else:
        if n[i] == "0":
            zero_s += 1
        else:
            one_s += 1

print(min(zero_s, one_s))