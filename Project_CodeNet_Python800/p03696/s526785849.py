N = int(input())
S = input()

left = ''
right = ''

skip_idx = []
for idx, s in enumerate(S):
    if idx in skip_idx:
        continue
    if s == ')':
        left += '('
    else:
        # print(j)
        skip_flag = 0
        for n in range(idx+1, N):
            if n in skip_idx:
                continue
            if S[n] == ')':
                skip_idx.append(n)
                skip_flag = 1
                break
        if not skip_flag:
            right += ')'
    # print(idx, s, left, right, skip_idx)

print(left+S+right)