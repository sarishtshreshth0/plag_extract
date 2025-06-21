#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [input() for _ in range(n)]

n = int(input())

i = 1
ans = 1000000000000
while i * i <= n:
    if (n % i == 0):
        a = i
        b = n//a
        a_keta = len(str(a))
        b_keta = len(str(b))
        m_keta = max(a_keta, b_keta)
        ans = min(ans, m_keta)
    i += 1
print(ans)




