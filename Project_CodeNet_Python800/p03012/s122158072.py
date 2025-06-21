N = int(input())
li = list(map(int,input().split()))

m = float('inf')

for i in range(len(li[:-1])):
    m_new = abs(sum(li[:i+1])-sum(li[i+1:]))
    m = min(m,m_new)
print(m)