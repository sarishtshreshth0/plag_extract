N = int(input())
A = list(map(int, input().split()))

cum_A = [A[0]]
for i in range(N-1):
    cum_A.append(cum_A[i] + A[i+1])
cum_A.insert(0, 0)    

cum_A_dict = dict()
for i in range(N+1):
    if cum_A[i] in cum_A_dict:
        cum_A_dict[cum_A[i]] += 1
    else:
        cum_A_dict[cum_A[i]] = 1

ans = 0
for v in cum_A_dict.values():
    if v == 1:
        pass
    else:
        ans += v*(v-1) // 2
        
print(ans)