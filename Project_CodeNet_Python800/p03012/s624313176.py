N = int(input())
W = list(map(int,input().split()))
sum_front_N = sum(W)
sum_back_N = 0
ans = sum_front_N
for i in W:
    sum_back_N +=i
    sum_front_N -=i
    ans = min(ans,abs(sum_front_N - sum_back_N))
print(ans)