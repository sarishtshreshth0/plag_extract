# Digits
N, K = map(int, input().split())
div = N // K
digits = []
while div > K:
    div = N // K
    digits.append(str(N % K))
    N   = div
digits.append(str(N % K))
if N // K != 0:
    digits.append(str(N // K))
ans = len(digits)
print(ans)