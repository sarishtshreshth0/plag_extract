n = int(input())
t = 0
s = set()
ans = 1
for i in range(n):
    w = input()
    if w[0] != t and i >= 1:
        ans = 0
        break
    t = w[-1]
    s.add(w)
if len(s) != n:
    ans = 0
print(["No","Yes"][ans])