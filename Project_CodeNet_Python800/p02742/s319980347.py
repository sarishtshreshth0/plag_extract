def main():
    H, W = map(int ,input().split())

    if H == 1 or W == 1:
        print(1)
        
    else:
        L1 = 0
        L2 = 0

        L1 = L2 = W // 2

        if W % 2 == 1:
            L1 += 1

        ans = (L1 + L2) * (H//2)

        if H % 2 == 1:
            ans += L1

        print(ans) 

if __name__ == "__main__":
    main()