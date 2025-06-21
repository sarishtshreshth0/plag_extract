def digits():
    # 入力
    N, K = map(int, input().split())
    # 処理
    count = 1
    while True:
        if N < K:
            return count
        else:
            N = N // K
            count += 1
            
result = digits()
print(result)