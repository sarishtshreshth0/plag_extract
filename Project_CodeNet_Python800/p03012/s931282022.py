N = int(input())
W = list(map(int,input().split()))

lst = [0]*(N-1)
S1 = [W[0]]*(N-1)
S2 = [sum(W)-W[0]]*(N-1)
lst[0] = abs(S1[0]-S2[0])

for i in range(1,N-1):
    S1[i] = S1[i-1]+W[i]
    S2[i] = S2[i-1]-W[i]
    lst[i] = abs(S1[i]-S2[i])

ans = min(lst)
print(ans)
