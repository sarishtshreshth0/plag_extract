a, b = (int(x) for x in input().split())
 
if a == 1 or b == 1:
    print("1")
elif a * b % 2 == 0:
    print(int(a * b / 2))
else:
    print(int((a * b - 1) / 2 + 1))