def main(H, W):
    if H == 1 or W == 1:
        return 1
    od = -(-W // 2)
    ev = W // 2
    ans = (od + ev) * (H // 2)
    if H % 2 == 1:
        ans += od
    return ans


if __name__ == "__main__":
    H, W = map(int, input().split())
    ans = main(H, W)
    print(ans)
