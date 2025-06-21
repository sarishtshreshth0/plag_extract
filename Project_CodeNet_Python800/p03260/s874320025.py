a, b = map(int, input().split())
num = []
for i in range(4):    
    if a * b * i % 2 != 0:
        num.append("Yes")
if "Yes" in num:
    print("Yes")
else:
    print("No")