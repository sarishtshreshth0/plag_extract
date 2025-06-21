N = int(input())
W = []
for i in range(N):
    W.append(input())

already = [W[0]]
out='Yes'
for i in range(1,N):
    if W[i-1][-1] != W[i][0]:
        out='No'
        break
    elif W[i] in already:
        out='No'
        break
    already.append(W[i])

print(out)