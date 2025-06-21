n, k = map(int, input().split())
q, count = n, 0
while(q >= k):
    r = q%k;      q = q//k
    count += 1
print(count+1)