def li():
    return list(map(int, input().split()))


def mi():
    return map(int, input().split())


def ii():
    return int(input())


H, W = mi()

# 移動できない
if H == 1 or W == 1:
    print(1)
# 縦偶数
elif H % 2 == 0:
    print(H * W // 2)
# 縦奇数 かつ　横偶数
elif W % 2 == 0:
    print(H * W // 2)
# 縦奇数 かつ　横奇数
else:
    print((H * W // 2) + 1)
