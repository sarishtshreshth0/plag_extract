N, A, B = map(int, input().split())
S = input()
a = 0
b = 0
for char in S:
    if char == 'a' and a+b < A+B:
        print("Yes")
        a += 1
    elif char == 'b' and a+b < A+B and b < B:
        print("Yes")
        b += 1
    else:
        print("No")