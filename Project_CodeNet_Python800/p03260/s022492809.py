a, b = list(map(int, input().split()))

if ((a*b*1) % 2 == 1) or ((a*b*2) % 2 == 1) or ((a*b*2) % 2 == 1):
    print("Yes")
else:
    print("No")