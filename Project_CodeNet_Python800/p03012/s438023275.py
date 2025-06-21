n = int(input())
w = list(map(int,input().split()))

wmin = []

w_sum = [w[0]]
for i in range(1,n):
    w_sum.append(w_sum[i-1] + w[i])

for i in range(n-1):
    wmin.append(abs(w_sum[n-1]-2*w_sum[i]))

print(min(wmin))
