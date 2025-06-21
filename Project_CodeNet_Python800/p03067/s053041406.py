a,b,c = map(int, input().split())
if a > b:
    a,b = b,a

for i in range(a, b+1):
    if i == c:
        print("Yes")
        exit()
print("No")