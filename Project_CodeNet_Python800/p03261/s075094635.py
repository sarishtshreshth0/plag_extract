n = int(input())

s_list = [input() for i in range(n)]

prev = s_list[0][-1]
ans = "Yes"
tmp = [s_list[0]]
for s in s_list[1:]:

    if s in tmp:
        ans = "No"
        break

    if s[0] != prev:
        ans = "No"
        break

    tmp.append(s)
    prev = s[-1]
print(ans)
