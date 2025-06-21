N = int(input())

w = [None] * N
for i in range(N):
    w[i] = input()

if len(w) != len(set(w)):
    print('No')
else:
    for i in range(1, N):
        if w[i-1][-1] != w[i][0]:
            print('No')
            break
    else:
        print('Yes')