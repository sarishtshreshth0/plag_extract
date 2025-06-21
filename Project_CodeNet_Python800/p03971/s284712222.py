n,a,b = map(int, input().split())
ab = a+b
S = input()
total = 0
b_total = 0
for s in S:
    if (s == "a" and total < ab):
        total += 1
        print("Yes")
    elif (s == "b" and total < ab and b_total < b):
        b_total += 1
        total += 1
        print("Yes")
    else:
        print("No")