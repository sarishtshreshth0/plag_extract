def main(H, W):
    if H == 1 or W == 1:
        return 1
    return -(-H * W // 2)


if __name__ == "__main__":
    H, W = map(int, input().split())
    ans = main(H, W)
    print(ans)
