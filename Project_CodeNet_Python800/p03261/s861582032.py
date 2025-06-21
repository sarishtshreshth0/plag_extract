def actual(n, W):
    # 重複があればアウト
    if len(set(W)) != len(W):
        return 'No'

    for i in range(len(W) - 1):
        word_now, word_next = W[i], W[i + 1]

        tail = word_now[-1]
        head = word_next[0]

        if tail != head:
            return 'No'

    return 'Yes'

N = int(input())
W = [input() for _ in range(N)]

print(actual(N, W))