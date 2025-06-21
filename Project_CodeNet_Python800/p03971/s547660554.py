N, A, B = map(int, input().split(' '))
S = input()

passed_a = 0
passed_b = 0
ans = []
for i in range(N):
    if S[i] == 'a':
        if passed_a + passed_b < A + B:
            ans.append('Yes')
            passed_a += 1
        else:
            ans.append('No')

    if S[i] == 'b':
        if passed_a + passed_b < A + B and passed_b < B:
            ans.append('Yes')
            passed_b += 1
        else:
            ans.append('No')

    if S[i] == 'c':
        ans.append('No')

for _ in ans:
    print(_)