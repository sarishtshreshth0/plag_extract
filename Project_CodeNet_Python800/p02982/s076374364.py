n, d = list(map(int, input().split()))
# A = list(map(int, input().split()))
#a = list(map(int, input().split()))
# data = [list(map(int, input().split())) for i in range(n)]
# q = int(input())
#a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# ab_sorted = sorted(ab, key=lambda x: x[0])
x = [list(map(int, input().split())) for i in range(n)]
# print(min(15*n, 100*(n//10+1), 100*(n//10)+15*(n % 10)))
# for i in range(1, int(n**0.5)+1):

count = 0
for i in range(n):
    for j in range(i+1, n):
        a = 0
        for k in range(d):
            # print(k)
            a += pow(x[i][k]-x[j][k], 2)
        # print(a)
        a = a**0.5
        if a == a//1:
            count += 1

print(count)
