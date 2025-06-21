N, A, B = [int(a) for a in input().split()]
S = input()
ans = []
npas = 0
npas_b = 0

for i in range(N):
    if S[i] == 'c':
        ans.append('No')
    else:
        if S[i] == 'a':
            if npas < A+B:
                ans.append('Yes')
                npas += 1
            else:
                ans.append('No')
        elif S[i] == 'b':
            if npas < A+B and npas_b < B:
                ans.append('Yes')
                npas += 1
                npas_b += 1
            else:
                ans.append('No')
                npas_b += 1

for a in ans:
    print(a)
