N = int(input())
M = N
sum = 0
while N > 0:
    sum += N % 10
    N = N // 10
print("Yes" if M % sum == 0 else "No")
