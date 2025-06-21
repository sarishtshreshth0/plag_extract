N = int(input())
S = input()
cnt = 0
post_c = ''
for i in range(len(S)):
    if post_c != S[i]:
        post_c = S[i]
        cnt += 1
print(cnt)
