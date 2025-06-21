H, W = list(map(int, input().split()))
### 片方だけ奇数のマスには行くことができない
### Hが偶数、Wが偶数の場合 → H*W // 2
### Hが奇数、Wが偶数の場合 → H*W // 2 (Wが奇数の場合も同様)
### Hが奇数、Wが奇数の場合 → H*W // 2 + 1
if H == 1 or W == 1:
    print(1)
elif H % 2 != 0 and W % 2 != 0:
    print(int(H * W // 2) + 1)
else:
    print(int(H * W // 2))