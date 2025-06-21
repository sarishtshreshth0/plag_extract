q, h, s, d = map(int, input().split())
n = int(input())
min_1l = min(q*4, h*2, s)
min_2l = min(min_1l*2, d)

print(min(n*min_1l, (n//2)*min_2l + (n%2)*min_1l))
