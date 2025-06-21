a, b, c = map(int, input().split())
for i in range(min(a,b)+1, max(a,b)):
    if i == c:
        print("Yes")
        exit()
print("No")