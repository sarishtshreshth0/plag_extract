N = int(input())
R = [tuple(map(int,input().split())) for _ in range(N)]
B = [tuple(map(int,input().split())) for _ in range(N)]

B.sort(key=lambda x: x[0])
# print(R)
# print(B)
ans =0
for b in B:
    candidate_R = [R[k] for k in range(len(R)) if (R[k][0] < b[0]) and (R[k][1] < b[1])] # 青い点に対する赤い点の候補
    if candidate_R:
        selected_R = sorted(candidate_R, key=lambda x:x[1])[-1]
        ans += 1
        R.remove(selected_R)
print(ans)
