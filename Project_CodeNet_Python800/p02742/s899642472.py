# パナソニックプログラミングコンテスト2020: B – Bishop
H, W = [int(i) for i in input().split()]

can_reach = 0
if H == 1 or W == 1:
    can_reach = 1
elif (H % 2 == 0 and W % 2 == 0) or (H % 2 == 0 and W % 2 == 1):
    can_reach = W * (H // 2)
elif H % 2 == 1 and W % 2 == 0:
    can_reach = W * (H // 2) + W // 2
else:
    can_reach = W * (H // 2) + W // 2 + 1

print(can_reach)