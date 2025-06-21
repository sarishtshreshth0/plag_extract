
A, B = map(int, input().split())
S = input()

if len(S) != A+B+1:
    print("No")
    exit()

for i in range(A+B+1):

    if i == A:
        if S[i] != "-":
            print('No')
            exit()
    else:
        if not('0' <= S[i] <= '9'):
            print('No')
            exit()
print('Yes')
