seen = set()

N = int(input())

prev = ""
for i in range(N):
    w = input()
    if w in seen:
        print("No")
        exit()
    seen.add(w)
    if i == 0:
        prev = w[-1]
        continue
    if prev != w[0]:
        print("No")
        exit()
    prev = w[-1]
print("Yes")
