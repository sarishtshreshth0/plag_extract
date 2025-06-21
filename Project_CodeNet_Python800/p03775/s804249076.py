N = int(input())

ans = 0

for i in range(1,int(N**0.5)+1):
    if N%i==0:
        ans = i

ans_len = max(len(str(ans)), len(str(N//ans)))

print(ans_len)