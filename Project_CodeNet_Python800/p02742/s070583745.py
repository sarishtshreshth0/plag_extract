def main():
    H, W = map(int, input().split())
    if H == 1 or W == 1:
        print(1)
        return
    B = W // 2
    A = W - B
    D = H // 2
    C = H - D
    print(C * A + D * B)
main()