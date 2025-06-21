A, B = map(int, input().split())
# 1..4k = 4k
# 1..(4k+1) = 1
# 1..(4k+2) = 4k+3
# 1..(4k+3) = 0

def xorall(aa):
    remz = aa % 4
    if remz == 0:
        return aa

    if remz == 1:
        return 1

    if remz == 2:
        return aa+1

    #if remz == 3:
    return 0

ans = xorall(B) ^ xorall(A-1)
print(ans)
