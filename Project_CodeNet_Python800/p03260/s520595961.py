a, b = map(int, input().split())
ans = False

for i in [1,2,3]:
    if (a * b * i) % 2 == 1:
        ans = True

if ans:
    print("Yes")
else:
    print("No")