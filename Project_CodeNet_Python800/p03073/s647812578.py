s = list(input())
now_1 = "0"
cnt_1 = 0
for i in range(len(s)):
    if s[i] != now_1:
        cnt_1 += 1
    if now_1 == "0":
        now_1 = "1"
    else:
        now_1 = "0"
now_2 = "1"
cnt_2 = 0
for i in range(len(s)):
    if s[i] != now_2:
        cnt_2 += 1
    if now_2 == "0":
        now_2 = "1"
    else:
        now_2 = "0"
print(min(cnt_1,cnt_2))