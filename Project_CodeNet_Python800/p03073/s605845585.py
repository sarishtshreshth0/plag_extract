s = input()

c01 = 0
c02 = 0

#01パターン
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] == "1":
            c01 += 1
    else:
        if s[i] == "0":
            c01 += 1

#10パターン
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] == "0":
            c02 += 1
    else:
        if s[i] == "1":
            c02 += 1

if all(x == 0 for x in [c01, c02]):
    print(0)
else:
    print(min(c01,c02))