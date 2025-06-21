N = int(input())
W_list = list(map(int, input().split()))

answer = 10**5
for i in range(N):
    answer = min(abs(sum(W_list[:i]) - sum(W_list[i:])), answer)
    
print(answer)