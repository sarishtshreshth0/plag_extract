s = list(input())
len_s = len(s)
half_len_s = len_s // 2 + 1
str_01 = "01" * half_len_s
str_10 = "10" * half_len_s
list_01 = list(str_01[:len_s])
list_10 = list(str_10[:len_s])
count1 = 0
count2 = 0
for v1, v2 in zip(s, list_01):
    if v1 == v2:
        count1 += 1
for v1, v2 in zip(s, list_10):
    if v1 == v2:
        count2 += 1
print(min(count1, count2))
