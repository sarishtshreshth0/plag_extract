H, W = map(int, input().split())
if (H == 1) or (W == 1):
    print(1)
    exit()
if H%2 == 1:
    if W%2 == 1:
        print(H*W//2 + 1)
        exit()
#     else:
#         print(H*W//2)
# else:
#     if W%2 == 1:
#         print(H*W//2)
#     else:
#         print(H*W//2)
print(H*W//2)