N = int(input())
W = list(map(int,input().split()))
# abs_list = list()
# for i in range(len(W)):
# 	abs_list.append(abs(sum(W[:i+1])-sum(W[i+1:])))
# print(min(abs_list))

W_sum = list()
W_sum.append(0)
for i in range(N):
	W_sum.append(W_sum[i] + W[i])

ans = 100000007
for i in range(len(W_sum)):
	ans = min(ans, abs((W_sum[N] - W_sum[i]) - W_sum[i]))

print(ans)
