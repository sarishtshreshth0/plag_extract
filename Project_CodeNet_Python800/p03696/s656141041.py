N = int(input())
S = input().rstrip()
cnt1, cnt2 = 0, 0
for s in S:
    if s == "(":
        cnt1 += 1
    if s == ")" and cnt1 >= 1:
        cnt1 -= 1
for s in reversed(S):
    if s == ")":
        cnt2 += 1
    if s == "(" and cnt2 >= 1:
        cnt2 -= 1
print("("*cnt2 + S + ")"*cnt1)