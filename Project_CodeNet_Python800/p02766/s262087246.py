N, K = map(int, input().split())
# NをK進数に変換
digits = ''
while N >= 1:
  digits += str(N % K)
  N //= K

print(len(digits))

