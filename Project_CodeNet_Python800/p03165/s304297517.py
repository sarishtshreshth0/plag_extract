S = input()
T = input()

s_len = len(S)
t_len = len(T)
ans_array = [[0] * (s_len + 1) for _ in range(t_len + 1)]

for t in range(1, t_len + 1):
    for s in range(1, s_len + 1):
        ans_array[t][s] = max(ans_array[t - 1][s], ans_array[t][s - 1])
        if T[t - 1] == S[s - 1]:
            ans_array[t][s] = ans_array[t - 1][s - 1] + 1

# ans_r = []

# s = s_len
# t = t_len

# while s > 0 and t > 0:
#     if ans_array[t][s] == ans_array[t - 1][s]:
#         t -= 1
#     elif ans_array[t][s] == ans_array[t][s - 1]:
#         s -= 1
#     else:
#         t -= 1
#         s -= 1
#         ans_r.append(S[s])

# print("".join(reversed(ans_r)))

ans_len = ans_array[-1][-1]
ans = [""] * ans_len
s_last = s_len
t_last = t_len
for i in range(ans_len - 1, -1, -1):
    s_next = 0
    t_next = 0
    for s in range(s_last, 0, -1):
        if ans_array[t_last][s] != ans_array[t_last][s - 1]:
            s_next = s
            break
    s_last = s_next
    for t in range(t_last, 0, -1):
        if ans_array[t][s_last] != ans_array[t - 1][s_last]:
            t_next = t
            break
    ans[i] = S[s_next - 1]
    s_last = s_next - 1
    t_last = t_next - 1

print("".join(ans))
