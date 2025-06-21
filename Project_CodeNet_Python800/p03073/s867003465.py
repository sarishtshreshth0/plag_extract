s = input()
n = int(len(s))
ans_1,ans_2 = 0,0

for i in range(n):
    if i % 2 == 0:
        t = "0"
    if i % 2 == 1:
        t = "1"
    if s[i] != t:
        ans_1 += 1

for i in range(n):
    if i % 2 == 0:
        t = "1"
    if i % 2 == 1:
        t = "0"
    if s[i] != t:
        ans_2 += 1

print(min(ans_1,ans_2))
