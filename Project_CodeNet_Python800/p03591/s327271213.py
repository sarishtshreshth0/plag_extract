s = list(input())
n = len(s)
t = list("YAKI")
for i in range(4):
    if not s[i % n] == t[i]:
        print("No")
        exit()
print("Yes")