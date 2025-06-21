def main():
    H,W = map(int,input().split())
    N = H*W
    #print(N//2)

    if H == 1 or W == 1:
        return 1
    elif N%2 == 0:
        ans = int(N/2)
    else:
        ans = int((N//2) + 1)

    return ans

print(main())
