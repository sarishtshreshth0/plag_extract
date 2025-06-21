C = 0
N = input()
num = N.split()
A = num[0]
B = num[1]
R = int(A) * int(B)
while C != 3:
    result = R * C
    if result % 2 == 0:
        C = C + 1
        if C == 3:
            print("No")
    elif result % 2 == 1:
        C = 3
        print("Yes")
