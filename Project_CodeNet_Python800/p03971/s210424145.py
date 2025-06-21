n, a, b = [int(w) for w in input().split()]
s = input()

n_li = [False] * n
pass_num = 0
b_rank = 0

for i, c in enumerate(s):
    if c == "a":
        if pass_num < a + b:
            n_li[i] = True
            pass_num += 1
    elif c == "b":
        b_rank += 1
        if pass_num < a + b and b_rank <= b:
            n_li[i] = True
            pass_num += 1


for t in n_li:
    print("Yes" if t else "No")
