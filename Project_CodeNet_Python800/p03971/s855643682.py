N, A, B = map(int, input().split())
S = input()

passed = 0
foreigners = 0

for i in range(N):
    # 国内学生
    if S[i] == "a":
        if passed < (A + B):
            passed += 1
            print("Yes")
        else:
            print("No")

    # 海外学生
    if S[i] == "b":
        foreigners += 1
        if passed < (A + B) and foreigners <= B:
            passed += 1
            print("Yes")
        else:
            print("No")

    if S[i] == "c":
        print("No")
