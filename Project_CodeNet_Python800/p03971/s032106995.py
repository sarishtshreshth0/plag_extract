N, A, B = map(int,input().split())
S = input()

Fore_rank = 1
passed = 0

for i in range(N):
    if S[i] == 'a' and A+B > passed:
        print("Yes")
        passed += 1
    elif S[i] == 'b' and A+B > passed and B >= Fore_rank:
        print("Yes")
        Fore_rank += 1
        passed += 1
    else: print("No")