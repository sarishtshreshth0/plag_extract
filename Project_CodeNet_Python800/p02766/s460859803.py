N, K = map(int, input().split())
answer = 0
while N // (K ** answer) >= 1:
    answer += 1
print(answer)