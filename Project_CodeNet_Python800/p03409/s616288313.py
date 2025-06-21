def solve():
    N = int(input())
    red = [list(map(int, input().split())) for _ in range(N)]
    blue = [list(map(int, input().split())) for _ in range(N)]
    blue.sort()
    red.sort(key=lambda x:-x[1])
    pairs = [False]*N
    for bx,by in blue:
        for i, (ax,ay) in enumerate(red):
            if pairs[i]==False and ay<by and ax<bx:
                pairs[i] = True
                break
    ans = pairs.count(True)
    return ans
print(solve())