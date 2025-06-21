N = int(input())
S = input()
Count = 1
for T in range(0,N-1):
    if S[T]!=S[T+1]:
        Count += 1
print(Count)