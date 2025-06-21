N = int(input())
W = list(map(int, input().split()))

ttl = sum(W)
s = []
min = ttl

for i in range(len(W)):
    s.append(W[i])
    s2 = ttl - sum(s)
    if abs(sum(s) - s2) < min:
        min = abs(sum(s) - s2)
        
print(min)