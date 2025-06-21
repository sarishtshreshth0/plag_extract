N = int(input())
S = input()
diff = [0] * (N + 1)
for i in range(N):
    if S[i] == "(":
        diff[i + 1] = diff[i] + 1
    else:
        diff[i + 1] = diff[i] - 1
min_diff = min(diff)
print("(" * -min_diff + S + ")" * (diff[N] - min_diff))
