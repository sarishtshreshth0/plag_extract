N = int(input())
D = set()
s = input().rstrip()
D.add(s)
s0 = s[-1]
for _ in range(N-1):
    s = input().rstrip()
    if s in D:
        print("No")
        exit()
    if s[0] != s0:
        print("No")
        exit()
    D.add(s)
    s0 = s[-1]
print("Yes")

