m, d = map(int, input().split())
print(sum(i%10 * m > m >= i//10*(i%10) for i in range(22, d+1)))