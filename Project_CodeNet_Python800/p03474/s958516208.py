A, B = map(int, input().split())
S = input()
f = True
for a in S[:A]:
    if not a.isdecimal():
        f = False
if S[A] != "-":
    f = False
for b in S[A+1:]:
    if not b.isdecimal():
        f = False
if f:
    print("Yes")
else:
    print("No")