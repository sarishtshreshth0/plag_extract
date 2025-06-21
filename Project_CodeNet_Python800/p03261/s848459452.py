N = int(input())
s = [input() for i in range(N)]
pre = ''
shirori = {}
for i in range(N):
    S = s[i]
    if i == 0:
        pre = S[len(S) - 1]
        shirori[S] = 1
        continue
    else:
        if shirori.get(S) is None:
            now = S[0]
            if now == pre:
                pre = S[len(S) - 1]
                shirori[S] = 1
            else:
                print('No')
                exit(0)
        else:
            print('No')
            exit(0)
print('Yes')
