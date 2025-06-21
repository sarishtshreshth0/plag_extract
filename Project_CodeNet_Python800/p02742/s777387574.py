H, W = map(int, input().split())

def solve(H,W):
    if H==1 or W==1:
        return 1
    ans = (H*W+1)//2
    return ans
print(solve(H,W))